#IMPORTANDO BIBLIOTECA
import os
import shutil

#CAMINHO PASTA

arquivos = "C:/Users/luiz.sampaio/Desktop/aula5/Arquivos_Lojas"

#LISTA OS ARQUIVOS

arquivos_excel = os.listdir (arquivos)

#CRIAR PASTAS COM NOMES DOS ESTADOS 

estados_temporarios = []

#SEPARAR ESTADOS

for item in arquivos_excel:
    #SEPARAR ESTADOS POR SIGLAS
    estado = item[-6:-4]
    #SEPARAR ESTADOS PARA CRIAÇÃO
    if estado not in estados_temporarios:
        estados_temporarios.append(estado)

#CRIAR PASTA
for estado in estados_temporarios:
     novo_dir = arquivos + '/' + estado + '/'
     diretorios_existentes = os.listdir(arquivos)
      #VERIFICANDO SE DIR JA EXISTE
"""if estado not in diretorios_existentes:
        os.mkdir(novo_dir)
      else:
          pass
"""
for item in arquivos_excel:
    #SEPARAR SIGLA
    estado = item[-6:-4]
    
    #CRIAR "DESTINO/"
    origem = arquivos + '/' + item
    
    #CRIAR "DESTINO/SP/NOME_DO_ARQUIVO"
    novo_destino = arquivos + '/' +  estado + '/' + item
    
    #MOVER PARA PASTA 
    shutil.move(origem, novo_destino)
 
#RETIRAR DA PASTA   
#LISTAR PASTAS
listar_pastas = "C:/Users/luiz.sampaio/Desktop/aula5/Arquivos_Lojas"

#LISTAR AS PASTAS COM ESTADO
estados = os.listdir(listar_pastas)

for i in estados:
  #CAMINHO DO ARQUIVOS
  caminho_completo = listar_pastas + '/' + i
  
  #
  arquivos = os.listdir(caminho_completo)
  
  for arquivo in arquivos:
    #
    caminho_arquivo = caminho_completo + '/' + arquivo
    
    shutil.move(caminho_arquivo, listar_pastas)  
  