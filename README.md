# Open Redirect Vulnerability Scanner

## Description

**Open Redirect Vulnerability Scanner** est un script Python interactif permettant de scanner un ou plusieurs domaines pour détecter des vulnérabilités de type open redirect.

Le script vous permet de choisir entre :

- Scanning d'un seul domaine
- Scanning d'une liste de domaines depuis un fichier `.txt`

### Fonctionnalités :

- Recherche automatique de liens potentiellement vulnérables à travers **waybackurls**
- Remplacement des paramètres de redirection pour détecter les redirections malveillantes
- Vérification des réponses HTTP pour confirmer la présence de redirections
- Affichage en couleur pour une meilleure lisibilité
- Message personnalisé lorsque aucune faille n'est trouvée

## Prérequis

Avant d'utiliser ce script, assurez-vous que les outils suivants sont installés sur votre machine :

- `waybackurls`
- `qsreplace`
- `curl`

Vous pouvez installer `qsreplace` avec la commande suivante :
```bash
go install github.com/tomnomnom/qsreplace@latest
```

## Installation
Clonez le dépôt sur votre machine locale :
```bash
git clone https://github.com/yaryatchii/Open-Redirect-Finder.git
```
## Accédez au dossier du projet :
```bash
cd Open-Redirect-Finder
```

## Utilisation
Lancez le script Python et suivez les instructions affichées :
```bash
python3 orvs.py
```

## Avertissement
Ce projet est destiné à des fins éducatives et de tests de sécurité uniquement. N'utilisez pas ce script pour scanner des domaines sans autorisation explicite.
