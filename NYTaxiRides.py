import pyspark
from pyspark.sql import functions
from pyspark.sql import SparkSession
from pyspark.sql.functions import unix_timestamp,udf,hour,minute,from_unixtime,date_format,year,month

print('criando sessao do spark')
spark = SparkSession\
    .builder\
    .appName("NYTaxiRides2Paquet")\
    .getOrCreate()

def createParquet():

    try:
        #reading csv files

        print('Iniciando a leitura dos arquivos de entrada')
        
        df = spark.read.option("header","true")\
            .option("inferschema","true")\
            .csv("/home/jovyan/2017_Yellow_Taxi_Trip_Data.csv")
        
        print('Arquivo carregado ao dataframe com sucesso')
        
       try:
            #iniciando a criação do arquivo em parquet
            print('Iniciando a criacao de arquivos em parquet')
            df.write.parquet('/home/jovyan/NY_TAXI_RIDES')#partitionBy("Year","Month")\
                
            print('Arquivos gerados com sucesso')
            print('Fim do pipeline')
        except:
            print('Erro ao escrever arquivo')
            raise
        

        #excluindo corridas zeradas
        #df = df[(df['fare_amount'] > 0)\
        #        | (df['total_amount'] > 0 )]
    except IOError as e:
        print("Erro ao ler o arquivo")
        raise

def payment_method():
    #metodo para criacao de dimensao de tipo de pagamentos
    print('Criando dimensao de tipo de pagamento ')
    dfPayment = dfPayment\
                .withColumn("Payment_des", functions\
                .when(dfPayment.Payment_type == 1, 'CREDIT CARD')
                .when(dfPayment.Payment_type == 2, 'CASH')
                .when(dfPayment.Payment_type == 3, 'NO CHARGE')
                .when(dfPayment.Payment_type == 4, 'DISPUTE')
                .when(dfPayment.Payment_type == 5, 'UNKNOWN')
                .otherwise('VOIDED TRIP')
                )
    dfPayment.write.parquet('/home/jovyan/NY_TAXI_RIDES'+'PAYMENT')
          
if __name__ == '__main__':
    #fazendo a chamada do metodo de conversao dos dados para parquet
    createParquet()
    
    #fazendo a chamado do metodo de criacao de dimensao de tipo de pagamentos
    payment_method()
