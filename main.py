import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import tensorflow as tf

from PIL import Image

# -----   To train the model --------

# from tensorflow.keras.datasets import cifar10 # type: ignore
# from tensorflow.keras.models import Sequential # type: ignore
# from tensorflow.keras.layers import Flatten, Dense # type: ignore
# from tensorflow.keras.utils import to_categorical # type: ignore

# # cifar10 is a datasets with 10 different categories
# (x_train, y_train), (x_val, y_val) = cifar10.load_data()
# # (preprocessing)
# x_train = x_train / 255
# x_val = x_val / 255  # for pixel values (preprocessing)

# y_train = to_categorical(y_train, 10)  
# y_val = to_categorical(y_val, 10)

# model = Sequential([
#     Flatten(input_shape=(32, 32, 3)), #32 pixels, 3 rgb colors
#     Dense(1000, activation='relu'),
#     Dense(10, activation='softmax')   # softmax is a function that converts logits to probabilities
# ])

# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(x_train, y_train, batch_size=64, epochs=10, validation_data=(x_val, y_val))
# model.save('cifar10_model.h5')


def main():
    st.title("Cifar10 Image Classification")
    st.write("Upload an image and the model will predict its class.")

    st.warning('This model can make mistakes.', icon="⚠️")
    file = st.file_uploader("Please Upload an Image", type=["jpg", "jpeg", "png"])
    
    if file:
        image = Image.open(file)
        st.image(image, caption='Uploaded Image', use_container_width=True)

        resized_image = image.resize((32, 32))
        img_array = np.array(resized_image) / 255
        img_array = img_array.reshape((1, 32, 32, 3))

        model = tf.keras.models.load_model('cifar10_model.h5')

        predictions = model.predict(img_array)
        cifar10_classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        fig, ax = plt.subplots()
        y_pos = np.arange(len(cifar10_classes))
        ax.barh(y_pos, predictions[0], align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(cifar10_classes)
        ax.invert_yaxis()
        ax.set_xlabel('Probability')
        ax.set_title('CIFAR-10 Class Predictions')
        
        st.pyplot(fig)

    else:
        st.text("You have not uploaded an image.")

if __name__ == "__main__":
    main()