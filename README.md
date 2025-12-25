# 📊 Système de Questionnaire PSM - Guide d'utilisation

## 🎯 Objectif
Ce système permet de collecter les réponses de vos étudiants sur l'acceptabilité des prix d'un produit/service et génère automatiquement les courbes de Van Westendorp pour analyser la sensibilité au prix.

## 📁 Fichiers inclus
- **questionnaire.html** : Formulaire que vos étudiants rempliront
- **results.html** : Page d'analyse avec graphiques et insights
- **README.md** : Ce fichier d'instructions

## 🚀 Comment utiliser le système

### Étape 1 : Héberger les fichiers
Vous avez plusieurs options :

#### Option A : Hébergement gratuit sur GitHub Pages (RECOMMANDÉ)
1. Créez un compte sur github.com
2. Créez un nouveau repository (dépôt) public
3. Uploadez les fichiers `questionnaire.html` et `results.html`
4. Activez GitHub Pages dans Settings → Pages → Source : main branch
5. Votre URL sera : `https://votre-nom.github.io/nom-du-repo/questionnaire.html`

#### Option B : Serveur local pour test rapide
```bash
# Dans le dossier contenant les fichiers, lancez :
python3 -m http.server 8000

# Puis accédez à : http://localhost:8000/questionnaire.html
```

#### Option C : Services d'hébergement gratuits
- **Netlify Drop** : Glissez-déposez vos fichiers sur netlify.com/drop
- **Vercel** : Importez votre dossier sur vercel.com
- **Neocities** : Hébergement gratuit sur neocities.org

### Étape 2 : Générer le QR Code

#### En ligne (FACILE) :
1. Allez sur **https://www.qr-code-generator.com/**
2. Sélectionnez "URL"
3. Collez l'URL de votre questionnaire
4. Personnalisez (optionnel) : couleurs, logo, design
5. Téléchargez le QR code en haute résolution (PNG ou SVG)

#### Avec Python :
```bash
# Installez la bibliothèque
pip install qrcode[pil]

# Générez le QR code
python3 -c "import qrcode; qr = qrcode.make('VOTRE_URL_ICI'); qr.save('qr_questionnaire.png')"
```

#### Avec un outil en ligne de commande :
```bash
# Avec qrencode
sudo apt-get install qrencode
qrencode -o qr_questionnaire.png "VOTRE_URL_ICI"
```

### Étape 3 : Projeter et collecter les réponses

1. **Projetez le QR code** sur l'écran de votre classe
2. Les étudiants scannent avec leur smartphone
3. Ils remplissent le questionnaire (2-3 minutes)
4. Les réponses sont sauvegardées automatiquement

### Étape 4 : Visualiser les résultats en temps réel

1. Ouvrez `results.html` sur votre ordinateur
2. Le graphique se met à jour automatiquement toutes les 10 secondes
3. Vous pouvez projeter cette page pour montrer l'évolution en direct

**Accès rapide aux résultats :**
- Cliquez sur le bouton 📊 en bas à droite du questionnaire

## 📈 Interprétation des courbes PSM

Le graphique affiche 4 courbes qui se croisent en plusieurs points clés :

### Les 4 courbes :
1. **Trop bon marché** (rouge) : % de personnes qui trouvent le prix suspicieusement bas
2. **Bon marché** (vert) : % de personnes qui trouvent le prix avantageux
3. **Cher** (jaune) : % de personnes qui trouvent le prix élevé
4. **Trop cher** (rouge clair) : % de personnes qui refusent d'acheter

### Points d'intersection importants :

| Intersection | Signification | Utilisation |
|--------------|---------------|-------------|
| **Bon marché ↔ Cher** | Prix optimal (OPP) | Prix recommandé pour maximiser la valeur perçue |
| **Trop bon marché ↔ Trop cher** | Prix marginal | Limite absolue du marché |
| **Trop bon marché ↔ Cher** | Limite inférieure | En dessous : risque de perception de faible qualité |
| **Bon marché ↔ Trop cher** | Limite supérieure | Au-dessus : trop de résistance à l'achat |

### Fourchette acceptable :
La zone entre la limite inférieure et la limite supérieure représente la **fourchette de prix acceptable** pour le marché cible.

## 🛠️ Fonctionnalités de la page Résultats

### Statistiques affichées :
- Nombre de réponses collectées
- Prix optimal calculé
- Prix idéal moyen déclaré
- Fourchette acceptable (min - max)

### Actions disponibles :
- **Exporter en CSV** : Télécharge toutes les données pour analyse dans Excel
- **Rafraîchir** : Met à jour les graphiques
- **Effacer les données** : Réinitialise pour un nouvel exercice

### Insights automatiques :
Le système génère automatiquement :
- Une recommandation de prix
- L'analyse de la cohérence entre prix optimal et prix idéal
- Des conseils stratégiques de positionnement

## 💡 Conseils pédagogiques

### Avant l'exercice :
1. Préparez un produit/service concret à évaluer (ex: "Abonnement mensuel à une plateforme de streaming de films belges")
2. Testez le système avec 2-3 réponses fictives
3. Préparez le QR code à projeter

### Pendant l'exercice :
1. Projetez le QR code (gardez-le affiché 5-10 minutes)
2. Expliquez l'objectif : "Nous allons déterminer scientifiquement le prix optimal"
3. Encouragez des réponses honnêtes (anonymat garanti)
4. Montrez les résultats en temps réel pendant la collecte

### Après l'exercice :
1. Analysez les courbes collectivement
2. Discutez des écarts entre "prix idéal" et "prix optimal"
3. Comparez avec les prix réels du marché
4. Exportez les données pour un exercice Excel complémentaire

## 🎓 Exercices complémentaires possibles

1. **Comparaison de segments** : Faire remplir pour différents profils (étudiants vs professionnels)
2. **Évolution temporelle** : Répéter l'exercice après présentation du produit
3. **A/B Testing** : Comparer deux descriptions différentes du même produit
4. **Analyse Excel** : Exporter et calculer médianes, quartiles, etc.

## 🔧 Dépannage

### Le QR code ne fonctionne pas :
- Vérifiez que l'URL est complète (avec https://)
- Testez l'URL dans un navigateur avant de générer le QR
- Augmentez la taille du QR code pour faciliter le scan

### Les résultats ne s'affichent pas :
- Vérifiez que les fichiers sont sur le même domaine/serveur
- Ouvrez la console développeur (F12) pour voir les erreurs
- Essayez de rafraîchir la page (Ctrl+R ou Cmd+R)

### Les données ont disparu :
- Les données sont stockées dans le navigateur (localStorage)
- Si vous changez de navigateur, les données ne suivent pas
- **Important** : Exportez régulièrement en CSV pour sauvegarder !

## 📱 Compatibilité

- ✅ Tous les smartphones (iOS, Android)
- ✅ Tous les navigateurs modernes (Chrome, Firefox, Safari, Edge)
- ✅ Tablettes et ordinateurs
- ✅ Fonctionne hors ligne après le premier chargement

## 🎨 Personnalisation

Vous pouvez modifier les couleurs et le design en éditant les fichiers HTML :
- Les couleurs principales sont définies dans la section `<style>`
- Le gradient de fond peut être changé dans `background: linear-gradient(...)`
- Les couleurs des courbes sont dans la fonction `createChart()`

## 📞 Support

Pour toute question ou amélioration :
- Consultez la documentation de la méthode PSM de Van Westendorp
- Référez-vous aux commentaires dans le code source
- Testez avec un petit groupe avant utilisation en classe

---

**Bonne analyse ! 🚀**
