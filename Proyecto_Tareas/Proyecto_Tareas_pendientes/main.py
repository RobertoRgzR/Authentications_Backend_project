from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import SQLModel, create_engine,Field,Session,select
from passlib.context import CryptContext
from typing import Optional
from jose import jwt,JWTError
from datetime import datetime,timedelta
from pydantic import BaseModel

            #Configuracion
#Motor de API'S
app = FastAPI()

#Creacion del moto de la base de datos
DATA_BASE = "sqlite:///database.db"
engine = create_engine(DATA_BASE)
#Creacion de base de datos
@app.on_event("startup")
def on_startup():    
    SQLModel.metadata.create_all(engine)

#Configuracion de TOKENS
secret_key = "Mi_clave_super_secreta_1234"
ALGORITHM = "HS256"

# HASHEO DE CONTRASEÑAS
pwd_context = CryptContext( 
schemes=["bcrypt"],
deprecated="auto"
)

# ==================================================
# OAUTH2
# ==================================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

#Creamos la clase usuario
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    username: str = Field(
        index=True,
        unique=True
    )

    email: str = Field(unique=True)

    hash_password: str

    is_active: bool = True

#Modelos de entrada
class UserCreate(BaseModel):
    username : str
    password : str
    email:str

class UserLogin(BaseModel):
    username : str
    password : str

#---------------FUNCIONES AUXILIARES------------------------------

#Funcion para Hashear las contraseñas

def hashing_password(password:str):
    return pwd_context.hash(password)

#Funcion para verificar contraseñas

def verify_password(plain_password:str,hash_password:str):
    return pwd_context.verify(plain_password,hash_password)

#Funcion para crear los tokens
def create_token(username:str):
    expire = datetime.utcnow() + timedelta(minutes=30)
    payload = {
    "sub": username,
    "role": "user",
    "active": True,
    "exp" : expire
}
    #Creacion del token: Pide 3 elementos()
    token = jwt.encode(payload,secret_key,algorithm=ALGORITHM)

    return token

#Funcion para validar el token y verificar que sea valido junto con queine es el que usa ese token
def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido"
    )

    try:

        payload = jwt.decode(
            token,
            secret_key,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")
        role = payload.get("role")
        active = payload.get("active")

        if username is None:
            raise credentials_exception

        return {
            "username": username,
            "role": role,
            "active": active
        }

    except JWTError:
        raise credentials_exception

    
    
#--------------------REGISTRO USUARIO-----------------------------

@app.post("/register")
def register_user(user_data:UserCreate):
    with Session(engine) as session:
        user_found = session.exec(select(User).where(User.username==user_data.username)).first()
        if user_found:
            raise HTTPException(status_code=400,detail="El usuario ya existe")
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            hash_password=hashing_password(
            user_data.password
    )
)

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return {
            "message": "Usuario registrado",
            "id": new_user.id
        }
    
#----------------LOGIN DEL USUARIO--------------------------
@app.post("/login")
def user_login(user_data:UserLogin):
    #Abrimos sesion para entrar a base de datos
    with Session(engine) as session:

        #Creamos una varibale donde haremos una busqueda en la base de datos si el username que nos dieron esta ahi

        user = session.exec(
            select(User).where(
                User.username == user_data.username
            )
        ).first()

        #Si el usuario no existe, lanzaremos un usuario o contraseña incorrectos

        if not user:

            raise HTTPException(
                status_code=401,
                detail="Usuario o contraseña incorrectos"
            )

        #Si la contraseña hasheada no es la correcta, retornaremos el mismo mensaje

        if not verify_password(
            user_data.password,
            user.hash_password
        ):

            raise HTTPException(
                status_code=401,
                detail="Usuario o contraseña incorrectos"
            )
        
        #Si el usuario y contraseña son correctos, creamos el token

        token = create_token(
            user.username
        )

        return {
            "access_token": token,
             "token_type": "bearer",
            "username": user.username
    }
    
# ==================================================
# RUTA PROTEGIDA
# ==================================================

@app.get("/profile")
def profile(
    current_user = Depends(get_current_user)
):

    return {
        "message": "Acceso autorizado",
        "usuario": current_user
    }

# ==================================================
# RUTA NORMAL
# ==================================================

@app.get("/")
def home():

    return {
        "mensaje": "API funcionando"
    }
