from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import schemas
from auth import authenticate_user, create_access_token, Annotated

app = FastAPI


@app.post("/token", response_model=schemas.Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],) -> schemas.Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"sub": user.username}
    )
    return schemas.Token(access_token=access_token, token_type="bearer")


# @app.get("/users/me", response_model=schemas.User)
# async def read_users_me(current_user: dict = Depends(get_current_user)) -> schemas.User:
#     return current_user
