from models.movimentacao.movimentacao import Movimentacao
from models.package.package import Package, PackageOut
from models.item.item import Item, ItemOut
from models.user.user import User
from models.user.user_out import UserOut
from fastapi import HTTPException

import datetime

class DB:
    movimentacoes = {
        1: Movimentacao(id_movimentacao=1, id_encomenda=1, endereco="Rua Quata, 300", status="Em trânsito", data=datetime.datetime.now()),
        2: Movimentacao(id_movimentacao=2, id_encomenda=1, endereco="Av. Cidade Jardim, 240", status="Em trânsito", data=datetime.datetime.now())
    }

    users = {
        1: User(id_user=1, nome="PA", sobrenome="Silva", email="pasilva@gmail.com", data_criacao=datetime.date(2021, 1, 1), status=True, senha="5139838273054835422"),
    }

    packages = {
        1: Package(id_package=1, id_user=1, data_criacao=datetime.date(2021, 1, 1), status=True),
    }

    items = {
        1: Item(id_item=1, nome="Celular", descricao="Celular ShaoMing", id_package=1, status=True),
    }


    movimentacoesNextID = 3
    usersNextID = 2
    packagesNextID = 2
    itemsNextID = 2

    @classmethod
    def movimentacoesIncID(cls):
        cls.movimentacoesNextID += 1

    @classmethod
    def usersIncID(cls):
        cls.usersNextID += 1
    
    @classmethod
    def packagesIncID(cls):
        cls.packagesNextID += 1
    
    @classmethod
    def itemsIncID(cls):
        cls.itemsNextID += 1

    @classmethod
    def getMovimentacao(cls, id):
        if id not in cls.movimentacoes:
            raise HTTPException(status_code=404, detail="Movimentação não encontrada")
        return cls.movimentacoes[id]
    
    @classmethod
    def getMovimentacoes(cls):
        return cls.movimentacoes.values()

    @classmethod
    def checkPackage(cls, id):
        if id not in cls.packages:
            raise HTTPException(status_code=404, detail="Encomenda não encontrada")
    
    @classmethod
    def getItems(cls,id_package):
        return list(map(lambda item: ItemOut(**item.model_dump()), filter(lambda item: item.id_package == id_package, cls.items.values())))
    
    @classmethod
    def genPackageOut(cls,package):
        package = PackageOut(**package.model_dump())
        package.produtos = cls.getItems(package.id_package)
        return package
    
    @classmethod
    def getPackage(cls, id):
        return cls.genPackageOut(cls.packages[id])
    
    @classmethod
    def getPackages(cls):
        return list(map(lambda package : cls.genPackageOut(package), cls.packages.values()))

    @classmethod
    def checkUser(cls, id):
        if id not in cls.users:
            raise HTTPException(status_code=404, detail="Usuário não encontrado") 
        
    @classmethod
    def getUsers(cls):
        return list(map(lambda user: UserOut(**user.model_dump()), cls.users.values()))
    
    @classmethod
    def getUser(cls, id):
        return UserOut(**cls.users[id].model_dump())
    
    @classmethod
    def checkItem(cls, id):
        if id not in cls.items:
            raise HTTPException(status_code=404, detail="Item não encontrado")
    
    @classmethod
    def getItem(cls, id):
        return ItemOut(**cls.items[id].model_dump())
    
    @classmethod
    def getAllItems(cls):
        return list(map(lambda item: ItemOut(**item.model_dump()), cls.items.values()))
    
    @classmethod
    def addItemToPackage(cls, id_package, id_item):
        cls.checkPackage(id_package)
        cls.checkItem(id_item)
        if cls.items[id_item].id_package is not None:
            raise HTTPException(status_code=404, detail="Item já está em outra encomenda")
        cls.items[id_item].id_package = id_package
