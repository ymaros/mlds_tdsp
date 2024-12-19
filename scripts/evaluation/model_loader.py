import tensorflow as tf
from tensorflow.keras.layers import Layer, Input, Dense, LSTM, Embedding, add, BatchNormalization
from tensorflow.keras.models import Model, load_model

class NotEqualLayer(Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def call(self, inputs):
        return tf.math.not_equal(inputs, 0)

def create_model(vocab_size, max_caption_length, cnn_output_dim):
    """Create the model architecture"""
    # Image input
    input_image = Input(shape=(cnn_output_dim,), name='Features_Input')
    fe1 = BatchNormalization()(input_image)
    fe2 = Dense(256, activation='relu')(fe1)
    fe3 = BatchNormalization()(fe2)
    
    # Caption input
    input_caption = Input(shape=(max_caption_length,), name='Sequence_Input')
    se1 = Embedding(vocab_size, 256, mask_zero=True)(input_caption)
    se2 = LSTM(256)(se1)
    
    # Decoder
    decoder1 = add([fe3, se2])
    decoder2 = Dense(256, activation='relu')(decoder1)
    outputs = Dense(vocab_size, activation='softmax', name='Output_Layer')(decoder2)
    
    # Create model
    model = Model(inputs=[input_image, input_caption], outputs=outputs, name='Image_Captioning')
    return model

def load_caption_model(model_path, weights_path=None):
    """
    Load the caption model with proper custom objects configuration
    """
    try:
        # Define custom objects
        custom_objects = {
            'NotEqualLayer': NotEqualLayer
        }
        
        # Try to load the model directly
        model = load_model(model_path, custom_objects=custom_objects)
        print("Model loaded successfully from .keras file")
        return model
    
    except Exception as e:
        print(f"Error loading model from .keras file: {str(e)}")
        print("Trying alternative loading method using weights...")
        
        try:
            # Model parameters (from training)
            vocab_size = 8586
            max_caption_length = 34
            cnn_output_dim = 2048
            
            # Create model architecture
            model = create_model(vocab_size, max_caption_length, cnn_output_dim)
            
            # Load weights if path provided
            if weights_path:
                model.load_weights(weights_path)
                print("Model weights loaded successfully")
            else:
                print("No weights path provided, using uninitialized model")
            
            return model
            
        except Exception as e:
            raise Exception(f"Failed to load model using both methods: {str(e)}")