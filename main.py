import argparse
from dpfm_model_runners.model_factory import model_factory
from PIL import Image

def parse_arguments():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Load a model and get image embeddings.")
    parser.add_argument('--image', type=str, required=True, help='Path to the image file.')
    parser.add_argument('--model', type=str, required=True, help='Model name to load.')

    # Parse and return the arguments
    return parser.parse_args()

def main():
    # Parse arguments
    args = parse_arguments()

    # Load the image
    your_image = Image.open(args.image)

    # Load the model, processor, and embedding function
    model_name = args.model
    model, processor, get_image_embedding = model_factory(model_name=model_name)

    # Get the image embedding
    image_embedding = get_image_embedding(your_image, None, None, None)

    # Print the result
    print("Image Embedding:", image_embedding)

if __name__ == "__main__":
    main()
