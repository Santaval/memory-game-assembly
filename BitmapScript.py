from PIL import Image

def main( argv ):
    if len(argv) < 2:
        print("Usage: python BitmapScript.py <image_path>")
        return 1

    matrix = bmp_to_matrix(argv[1])
    matrix = normalize_matrix(matrix)
    get_nonzero_pixels(matrix)
    # for i in range(len(matrix)):
    #     print(len(matrix[i]))


# Función para convertir una imagen BMP a una matriz de bits
def bmp_to_matrix(file_path):
    # Abrir la imagen BMP
    image = Image.open(file_path)

    # Obtener los datos de píxeles
    pixel_data = list(image.getdata())

    # Obtener las dimensiones de la imagen
    width, height = image.size

    # Crear una matriz para almacenar los valores de los píxeles
    matrix = [[0] * width for _ in range(height)]

    # Llenar la matriz con los valores de los píxeles
    for i in range(height):
        for j in range(width):
            matrix[i][j] = pixel_data[i * width + j]

    return matrix

# transform matrix into values 0 and 1 if the value is 0 or 255
def normalize_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            average = (matrix[i][j][0] + matrix[i][j][1] + matrix[i][j][2] + matrix[i][j][3]) / 4
            if average < 64:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
    return matrix

def get_nonzero_pixels(matrix):
    nonzero_cols = []
    nonzero_rows = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                nonzero_cols.append(j)
                nonzero_rows.append(i)

    print("Nonzero rows: \n ", nonzero_rows)
    print("Nonzero rows lenght: \n", len(nonzero_rows))
    print("Nonzero cols: \n", nonzero_cols)
    print("Nonzero cols lenght: \n", len(nonzero_cols))


if __name__ == "__main__":
    import sys
    main(sys.argv)
