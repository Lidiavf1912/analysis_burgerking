import pandas as pd

#CREAR DICCIONARIO CON LOS NOMBRES DE LAS COLUMNAS Y SUS TIPOS
def create_dictio(df):

    column_types= {}

    for e in df:

        if ('float' in str(df[e].dtype)):
            column_types[e]='FLOAT'

        elif ('int' in str(df[e].dtype)):
            column_types[e]='INT'

        else:
            column_types[e]='VARCHAR(100)'
        

    return column_types
        

#CREAR TABLAS
def create_table(table_name, column_names_types, cursor):
    """
    Function that receives the name of the table "table_name", 
    a dictionary "column_names_types" with the format 
    key (column name): value(column type)  

    Returns the string with the query for create table

    """

    cursor.execute(f'DROP TABLE IF EXISTS `{table_name}`;\n')
    
    # Añadir CREATE TABLE
    query = f'CREATE TABLE `{table_name}`('

    # Añadir todas las columnas a la cadena desde el diccinario
    for key, value in column_names_types.items():

        query += f'{key} {value}, '

    cursor.execute(query[:-2] + ');')

def create_tables(db_structure, dframes, cursor):
        
    for table, keys in db_structure.items():
        #Read dataframe
        
        #Crear tabla con dataframe
        create_table(table, create_dictio(dframes[table]), cursor)
        
        # Revisar y añadir las primary keys
        if 'primary_keys' in keys:
            primary_keys_str = ', '.join([f'`{pk}`' for pk in keys['primary_keys']])
            primary_key_query = f'ALTER TABLE `{table}` ADD PRIMARY KEY ({primary_keys_str});'
            cursor.execute(primary_key_query)

        if 'foreign_keys' in keys:
            for fk_info in keys['foreign_keys']:
                foreign_key_str = ', '.join([f'`{fk}`' for fk in fk_info['fk']])
                reference_str = f"`{fk_info['reference_table']}` (`{fk_info['reference_column']}`)"
                foreign_key_query = f'ALTER TABLE `{table}` ADD FOREIGN KEY ({foreign_key_str}) REFERENCES {reference_str};'
                cursor.execute(foreign_key_query)

        #Añadir valores
        insert_values(table, dframes[table], cursor)


#AÑADIR VALORES
def insert_values(table_name, df, cursor):

    column_names = ','.join(df.columns)

    # Para cada fila

    for i in range(df.shape[0]):   
        
        values = tuple(df.iloc[i].values)   
        
        cursor.execute(f'insert into `{table_name}` ({column_names}) values {values};')


