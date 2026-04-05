import os
import sys
from PIL import Image

def greek_to_greeklish(text):
    """Μετατρέπει ελληνικούς χαρακτήρες σε λατινικούς."""
    mapping = {
        'α': 'a', 'β': 'b', 'γ': 'g', 'δ': 'd', 'ε': 'e', 'ζ': 'z', 'η': 'i', 'θ': 'th',
        'ι': 'i', 'κ': 'k', 'λ': 'l', 'μ': 'm', 'ν': 'n', 'ξ': 'x', 'ο': 'o', 'π': 'p',
        'ρ': 'r', 'σ': 's', 'τ': 't', 'υ': 'y', 'φ': 'f', 'χ': 'ch', 'ψ': 'ps', 'ω': 'o',
        'ς': 's', 'ά': 'a', 'έ': 'e', 'ή': 'i', 'ί': 'i', 'ό': 'o', 'ύ': 'y', 'ώ': 'o',
        'ϊ': 'i', 'ϋ': 'y', 'ΐ': 'i', 'ΰ': 'y',
        'Α': 'A', 'Β': 'B', 'Γ': 'G', 'Δ': 'D', 'Ε': 'E', 'Ζ': 'Z', 'Η': 'I', 'Θ': 'TH',
        'Ι': 'I', 'Κ': 'K', 'Λ': 'L', 'Μ': 'M', 'Ν': 'N', 'Ξ': 'X', 'Ο': 'O', 'Π': 'P',
        'Ρ': 'R', 'Σ': 'S', 'Τ': 'T', 'Υ': 'Y', 'Φ': 'F', 'Χ': 'CH', 'Ψ': 'PS', 'Ω': 'O',
        'Ά': 'A', 'Έ': 'E', 'Ή': 'I', 'Ί': 'I', 'Ό': 'O', 'Ύ': 'Y', 'Ώ': 'O'
    }
    return "".join(mapping.get(char, char) for char in text)

def resize_images(input_folder, target_width, force_jpeg=False, use_greeklish=False):
    # Δημιουργία ονόματος φακέλου εξόδου
    folder_name = f"Resized_{target_width}"
    if force_jpeg: folder_name += "_as_JPEG"
    if use_greeklish: folder_name += "_En"
        
    output_folder = os.path.join(input_folder, folder_name)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            img_path = os.path.join(input_folder, filename)
            
            try:
                # 1. Καθαρισμός ονόματος: Πάντα αντικατάσταση κενού με παύλα
                new_filename = filename.replace(" ", "-")

                # 2. Προαιρετικά Greeklish
                if use_greeklish:
                    new_filename = greek_to_greeklish(new_filename)

                # 3. Επεξεργασία εικόνας
                with Image.open(img_path) as img:
                    if force_jpeg:
                        img = img.convert("RGB")
                        file_root = os.path.splitext(new_filename)[0]
                        new_filename = f"{file_root}.jpg"

                    # Resize με διατήρηση aspect ratio
                    w_percent = (target_width / float(img.size[0]))
                    h_size = int((float(img.size[1]) * float(w_percent)))
                    resized_img = img.resize((target_width, h_size), Image.Resampling.LANCZOS)
                    
                    output_path = os.path.join(output_folder, new_filename)
                    
                    if force_jpeg:
                        resized_img.save(output_path, "JPEG", quality=90, optimize=True)
                    else:
                        resized_img.save(output_path, quality=90, optimize=True)
                        
                    print(f"[OK] {filename} -> {new_filename}")
            except Exception as e:
                print(f"[ERROR] Σφάλμα στο {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Χρήση: python resize.py <φάκελος> <πλάτος> [jpeg] [greeklish]")
        sys.exit(1)

    folder = sys.argv[1]
    # Αφαίρεση εισαγωγικών αν υπάρχουν από το drag and drop στα Windows
    folder = folder.strip('"')
    
    try:
        width = int(sys.argv[2])
    except ValueError:
        print("Σφάλμα: Το πλάτος πρέπει να είναι αριθμός!")
        sys.exit(1)
    
    # Έλεγχος παραμέτρων (case insensitive)
    args_lower = [arg.lower() for arg in sys.argv]
    convert_to_jpeg = "jpeg" in args_lower
    convert_to_greeklish = "greeklish" in args_lower

    if os.path.isdir(folder):
        resize_images(folder, width, convert_to_jpeg, convert_to_greeklish)
        print("\nΗ επεξεργασία ολοκληρώθηκε επιτυχώς!")
    else:
        print(f"Σφάλμα: Ο φάκελος '{folder}' δεν βρέθηκε.")