from ez_wsi_dicomweb import credential_factory, patch_embedding_endpoints, patch_embedding, local_image

class GoogleLoader:
    def __init__(self):
        self.credentials = credential_factory.DefaultCredentialFactory()
        self.endpoint = patch_embedding_endpoints.V2PatchEmbeddingEndpoint(credential_factory=self.credentials)

        def preprocess(img):
            return img
        def create_model(img):
            model = patch_embedding.get_patch_embedding(self.endpoint, img)
            return model

        self.model = create_model
        self.processor = preprocess

    def get_processor_and_model(self):
        return self.processor, self.model


    # Function to get image embedding
    def get_image_embedding(self, image, processor=None, model=None, device=None):
        # Construct an image from the in memory patch
        image = local_image.LocalImage(image)
        # Define coordinates of image patch
        patch = image.get_patch(x=0, y=0, width=224, height=224)

        embedding = patch_embedding.get_patch_embedding(self.endpoint, patch)
        return embedding



