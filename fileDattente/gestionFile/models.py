# from django.db import models

# Create your models here.

import mysql.connector
from mysql.connector import errorcode
from django.db import models

class ClientQueueManager:
    @staticmethod
    def send_message(sql, sql2='SELECT @retour'):
        print("###########           Connexion reussie")
        try:
            # Connexion à la base de donnees
            con = mysql.connector.connect(
                host='localhost', user='root', password='', database='filedattente')
            print("###########           Connexion reussie")
            # con.autocommit = True
            cursor = con.cursor()
            # Execution d'une requete SELECT
            cursor.execute(sql)
            if((sql2 != None) and (len(sql2) > 0)):
                cursor.execute(sql2)
            # Recuperation des resultats
            rows = cursor.fetchall()
            return rows
            # con.commit();
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            con.close()

    @staticmethod
    def executeCommand(command):
        command = command.lower()
        if(command == 'add_client'):  # Choix d'ajout d'un client dans la file d'attente
            return ClientQueueManager.add_client()
        # Choix d'ajout d'une cliente en état de grossesse dans la file d'attente
        elif(command == 'add_pregnant'):
            return ClientQueueManager.add_pregnant()
        elif(command == 'add_senior'):  # Choix d'ajout d'un client senior dans la file d'attente
            return ClientQueueManager.add_senior()
        elif(command == 'pop_first'):  # Choix de récupération du client en tête de la file d'attente
            return ClientQueueManager.pop_first_client()
        elif(command == 'count'):  # Choix d'affichage du nombre de clients dans la file d'attente
            return ClientQueueManager.get_queue_length()
        elif(command == 'get_all'):  # Choix d'affichage des clients de la file d'atten
            return ClientQueueManager.get_all_clients()

    @staticmethod
    def add_client():
        rows = ClientQueueManager.send_message('CALL add_client(@retour);')
        if(len(rows) > 0):
            return rows[0][0]

    @staticmethod
    def add_pregnant():
        rows = ClientQueueManager.send_message(
            'CALL add_pregnant_client(@retour)')
        if(len(rows) > 0):
            return rows[0][0]

    @staticmethod
    def add_senior():
        rows = ClientQueueManager.send_message(
            'CALL add_senior_client(@retour)')
        if(len(rows) > 0):
            return rows[0][0]

    @staticmethod
    def pop_first_client():
        rows = ClientQueueManager.send_message('CALL pop_first(@retour)')
        if(len(rows) > 0):
            return rows[0][0]

    @staticmethod
    def get_queue_length():
        rows = ClientQueueManager.send_message('CALL get_length(@retour)')
        if(len(rows) > 0):
            return rows[0][0]

    @staticmethod
    def get_all_clients():
        try:
            # Recuperation de la file
            rows = ClientQueueManager.send_message(
                'SELECT _number, arrival, next_client_number FROM client', sql2=None)
            if(rows == None or len(rows) == 0):
                return []
            # re-organisation des donnees
            dic = {}
            for row in rows:
                dic[row[0]] = row
            # recuperation de la tete de file
            rows = ClientQueueManager.send_message(
                'SELECT top FROM params WHERE id=1', sql2=None)
            nextClient = rows[0][0]
            # Trie de la file d'attente
            rows = []
            while True:
                row = dic[nextClient]
                rows.append(row)
                nextClient = row[2]
                if(nextClient == None):
                    break
            return str(rows)
        except ValueError:
            return []

# Test du fonctionnement
# commands = [
    # { 'command' : 'ADD_CLIENT', 'nb' : 4},
    # { 'command' : 'ADD_SENIOR', 'nb' : 2},
    # { 'command' : 'ADD_PREGNANT', 'nb' : 1},
    # { 'command' : 'ADD_CLIENT', 'nb' : 2},
    # { 'command' : 'ADD_SENIOR', 'nb' : 1},
    # { 'command' : 'ADD_CLIENT', 'nb' : 3},
    # { 'command' : 'ADD_PREGNANT', 'nb' : 1},
    # { 'command' : 'GET_ALL', 'nb' : 1}
# ]

# for elt in commands:
    # for i in range(elt['nb']):
        # response_data = ClientQueueManager.executeCommand(elt['command'])
        # print(' -->> ' + response_data)


# from multiprocessing.connection import Client
# from django.db import models


# class Client(models.Model):
#     _number = models.IntegerField(primary_key=True)
#     arrival = models.DateField()
#     next_client_number = models.ForeignKey(Client, on_delete=models.CASCADE)

#     def __str__(self):
#         return self._number


# class Params(models.Model):
#     id = models.IntegerField(primary_key=True)
#     top = models.ForeignKey(Client, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.id


class Personnel(models.Model):
    idPersonnel = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    profil = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    empAuth_objects = models.Manager()


# class Guichet(models.Model):
#     numGuichet = models.IntegerField(primary_key=True)
#     idPersonnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.numGuichet
