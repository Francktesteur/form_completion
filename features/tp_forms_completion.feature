# Created by fbouchaud2024 at 28/02/2025
Feature: Compléter un formulaire
  # Compléter le formulaire sur le lien http://localhost:63342/05%20-%20Forms%20Completion/inscription.html?_ijt=sp7ic72dgr2or59m28qo9dsgld&_ij_reload=RELOAD_ON_SAVE

  Scenario: Remplir un formulaire d'inscription sur lesite eni tech community
      Given Je suis sur la page formulaire d'inscrition Eni Tech Community
      When Je saisis un email valide "auyayah@kgmil.com" dans le champ email
      And Je saisis un mot de passe valide "motdepasse" dans le champ mot de passe
      And Je saisis une adresse valide "5 rue Franklyn" dans le champ addresse
      And Je saisis un code postal valide "44100" dans le champ code postal
      And Je saisis une ville "Nantes" dans le champ ville
      And Je choisis "France" dans la liste déroulante pays
      And Je clique sur le bouton valider
      Then J'ai un message Inscrption réussite !



