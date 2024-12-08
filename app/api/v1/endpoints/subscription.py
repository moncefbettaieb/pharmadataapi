from fastapi import APIRouter, Depends, HTTPException
from app.db.session import database
from app.db.models.user import users
from app.schemas.subscription import SubscriptionUpdate, SubscriptionStatus
from app.api.dependencies import get_current_user
from app.core.subscriptions import subscription_quotas

router = APIRouter()

@router.get("/me", response_model=SubscriptionStatus)
async def get_subscription_status(current_user = Depends(get_current_user)):
    quota = current_user["quota"] if current_user["quota"] is not None else 100
    usage = current_user["usage"] if current_user["usage"] is not None else 0
    remaining = quota - usage
    return SubscriptionStatus(
        subscription_level=current_user["subscription_level"],
        usage=current_user["usage"],
        quota=current_user["quota"],
        remaining=remaining
    )

@router.post("/", response_model=SubscriptionStatus)
async def update_subscription(
    sub: SubscriptionUpdate,
    current_user = Depends(get_current_user)
):
    if sub.level not in subscription_quotas:
        raise HTTPException(status_code=400, detail="Niveau d'abonnement invalide")

    # Définir le nouveau quota depuis la table subscription_quotas
    new_quota = subscription_quotas[sub.level]

    # Mettre à jour l'utilisateur dans la base de données
    query = users.update().where(users.c.id == current_user["id"]).values(
        subscription_level=sub.level,
        quota=new_quota,
        usage=0  # On réinitialise la consommation lors d'un changement d'abonnement
    )
    await database.execute(query)

    # Récupérer les informations mises à jour
    query = users.select().where(users.c.id == current_user["id"])
    updated_user = await database.fetch_one(query)

    remaining = updated_user["quota"] - updated_user["usage"]
    return SubscriptionStatus(
        subscription_level=updated_user["subscription_level"],
        usage=updated_user["usage"],
        quota=updated_user["quota"],
        remaining=remaining
    )
