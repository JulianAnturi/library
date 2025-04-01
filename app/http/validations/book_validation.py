
class BookValidation:
    def __init__(self)->None:
        pass

    @staticmethod
    def validate_book_data(data ):
        errors = []

        isbn = data.get('isbn')
        url = data.get('url')
        state = data.get('state')
        quantity = data.get('quantity')
        price = data.get('price')
        sypnosis = data.get('sypnosis')

        if not isbn or len(isbn) > 20:
            errors.append("ISBN es obligatorio y debe tener máximo 20 caracteres.")

        if not url or len(url) > 255:
            errors.append("URL es obligatoria y debe tener máximo 255 caracteres.")

        if state not in [1, 2, 3]:
            errors.append("El estado debe ser 1 (disponible), 2 (prestado) o 3 (comprado).")

        if not isinstance(quantity, int) or quantity < 0:
            errors.append("La cantidad debe ser un número entero positivo.")

        if not isinstance(price, (int, float)) or price < 0:
            errors.append("El precio debe ser un número positivo.")

        if not sypnosis or len(sypnosis.strip()) == 0:
            errors.append("La sinopsis no puede estar vacía.")

        return errors
