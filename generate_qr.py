#!/usr/bin/env python3
"""
Script pour générer un QR code pour le questionnaire PSM
Usage: python3 generate_qr.py URL_DU_QUESTIONNAIRE
"""

import sys
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SquareGradiantColorMask

def generate_qr_code(url, output_file="qr_questionnaire.png"):
    """
    Génère un QR code stylisé pour l'URL donnée
    
    Args:
        url (str): L'URL du questionnaire
        output_file (str): Nom du fichier de sortie
    """
    # Créer le QR code
    qr = qrcode.QRCode(
        version=1,  # Taille automatique
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Haute correction d'erreur
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    # Générer l'image avec style
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=SquareGradiantColorMask(
            back_color=(255, 255, 255),
            center_color=(44, 95, 141),  # Bleu du thème
            edge_color=(74, 123, 167)    # Bleu clair du thème
        )
    )
    
    # Sauvegarder
    img.save(output_file)
    print(f"✅ QR code généré avec succès : {output_file}")
    print(f"📱 URL encodée : {url}")
    print(f"📏 Taille recommandée pour projection : A4 (21 x 21 cm minimum)")

def generate_simple_qr(url, output_file="qr_questionnaire_simple.png"):
    """
    Génère un QR code simple (sans dépendances supplémentaires)
    
    Args:
        url (str): L'URL du questionnaire
        output_file (str): Nom du fichier de sortie
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="#2C5F8D", back_color="white")
    img.save(output_file)
    
    print(f"✅ QR code simple généré : {output_file}")
    print(f"📱 URL encodée : {url}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Erreur : URL manquante")
        print()
        print("Usage:")
        print("  python3 generate_qr.py URL_DU_QUESTIONNAIRE")
        print()
        print("Exemples:")
        print("  python3 generate_qr.py https://votre-site.github.io/questionnaire.html")
        print("  python3 generate_qr.py http://localhost:8000/questionnaire.html")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Vérifier que l'URL commence par http:// ou https://
    if not url.startswith(('http://', 'https://')):
        print("⚠️  Attention : L'URL devrait commencer par http:// ou https://")
        print(f"   URL fournie : {url}")
        response = input("   Continuer quand même ? (o/n) : ")
        if response.lower() != 'o':
            sys.exit(0)
    
    try:
        # Essayer de générer la version stylisée
        generate_qr_code(url)
        print()
        print("💡 Conseil : Pour un QR code simple sans style, utilisez :")
        print(f"   python3 generate_qr.py {url} simple")
    except ImportError:
        # Si les dépendances pour le style ne sont pas disponibles
        print("ℹ️  Génération d'un QR code simple (dépendances de style non disponibles)")
        generate_simple_qr(url)
        print()
        print("💡 Pour un QR code stylisé, installez :")
        print("   pip install qrcode[pil]")
    except Exception as e:
        print(f"❌ Erreur lors de la génération : {e}")
        print("Tentative avec QR code simple...")
        try:
            generate_simple_qr(url)
        except Exception as e2:
            print(f"❌ Échec complet : {e2}")
            sys.exit(1)
