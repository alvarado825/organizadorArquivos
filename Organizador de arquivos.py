import os
import shutil


while(1):
    extensao = '.' + input('Digite a extensão dos arquivos a serem movidos: ').lower()
    caminho = input('Digite o caminho dos arquivos a serem movidos: ')
    caminho_novo = caminho + r'\Arquivos ' + extensao.replace('.','')
    contador = 0
    repetidos = 0

    try:
        print('Criando a pasta para agrupar os arquivos...')
        os.mkdir(caminho_novo)
        
    except FileExistsError as e:
        print('Uma pasta para este arquivo já foi criada, Esvazie a pasta.. \n')
    except Exception as e:
        print(f'Erro: {e}')
        
    for root, dirs, files in os.walk(caminho):
        
        for file in files:
            if extensao in file:
                new_path = os.path.join(caminho_novo, file)
                old_path = os.path.join(root, file)
                files_2 =[filess for roots, dirss, filess in os.walk(caminho_novo)]
                
                if file in files_2[0]:
                    repetidos += 1
                    new_path = os.path.join(caminho_novo, file.replace(extensao, f'({str(repetidos)}){extensao}'))
                    shutil.move(old_path, new_path)
                    print(f'Arquivo Repetido {file} movido para pasta {caminho_novo}\n')
                else:  
                    shutil.move(old_path, new_path)
                    print(f'Arquivo {file} movido para pasta {caminho_novo}\n')
                

                contador += 1
                
        break
        
    print(f'Total de {contador} arquivos movidos')
     



