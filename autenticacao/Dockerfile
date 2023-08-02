#Baixa o python 3.9 no docker
FROM python:3.9

#Copia o requirements.txt e instala as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Copia todo o projeto para a pasta /projeto dentro do docker
COPY . /projeto

#Entra no diretório /projeto dentro do docker
WORKDIR /projeto

#Expõe a porta 8000
EXPOSE 8000

#Roda o projeto
ENTRYPOINT [ "python", "autenticacao/manage.py" ]
CMD ["runserver", "0.0.0.0:8000"]