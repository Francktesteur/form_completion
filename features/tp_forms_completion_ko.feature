# Created by fbouchaud2024 at 28/02/2025
Feature: Compléter un formulaire avec des informations non valide
  # Enter feature description here

    Scenario Outline:Remplir le formulaire avec des informations obligatoires manquantes
      Given Je suis sur la page formulaire d'inscrition Eni Tech Community avec les champs apparants
      When Je saisis un email  "<email>" dans le champ email
      And  Je saisis un mot de passe  "<password>" dans le champ mot de passe
      And Je saisis une adresse "<adresse>" dans le champ addresse
      And Je saisis un code postal  "<zipcode>" dans le champ code postal
      And Je saisis une ville "<city>" dans le champ ville
      And Je choisis "<states>" dans la liste déroulante pays
      And Je clique sur le bouton valider

      Examples:
          |email            |password |adresse          |zipcode |city    |states|
          |fanfisd@gmail.com|dfg44    |4 rue de la ddd  |44100   |Nantes  |France|
          |                 |zfd45    |5 rue deeee      |45000   |val     |France|
          |cefafcc@gmail.fr |         |4 rue de la ddd  |44000   |Vertou  |France|