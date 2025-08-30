name: "🖼️ Image Classifier - AI App"

description: >
  A simple AI-powered Image Classification Web App built with Streamlit and TensorFlow.
  This app classifies images into one of the 10 CIFAR-10 categories using a pre-trained deep learning model.

demo: "https://himanshu-model-image-classifier.streamlit.app/"

features:
  - "📤 Upload any image directly from your device"
  - "🤖 Get instant predictions from a trained deep learning model"
  - "🎨 Visualize results with clean UI using Streamlit"
  - "☁️ Deployable on Streamlit Cloud"

project_structure:
  - "images/ : Sample images"
  - "cifar10_model.h5 : Pre-trained model"
  - "main.py : Streamlit app script"
  - "requirements.txt : Dependencies"
  - "README.md : Project documentation"

installation_and_setup:
  clone_repository: |
    git clone https://github.com/himanshu2285/Image-Classifier.git
    cd Image-Classifier

  create_virtual_environment:
    linux_mac: |
      python -m venv venv
      source venv/bin/activate
    windows: |
      python -m venv venv
      venv\Scripts\activate

  install_dependencies: |
    pip install -r requirements.txt

  run_locally: |
    streamlit run main.py
    # Then open http://localhost:8501 in your browser

dataset_info:
  name: "CIFAR-10"
  total_images: "60,000"
  image_size: "32x32 color images"
  classes:
    - "✈️ Airplane"
    - "🚗 Automobile"
    - "🐦 Bird"
    - "🐱 Cat"
    - "🦎 Deer"
    - "🐕 Dog"
    - "🐸 Frog"
    - "🐎 Horse"
    - "🚢 Ship"
    - "🚚 Truck"

usage_example:
  steps:
    - "Upload an image (e.g., a cat or car picture)."
    - "The model processes it and predicts the most likely class."
    - "Results are displayed instantly with probability scores."

contributing: >
  Contributions, issues, and feature requests are welcome!
  Feel free to fork this repo and submit pull requests.

license: "MIT License"

author:
  name: "Himanshu Mishra"
  links:
    github: "https://github.com/himanshu2285"
    linkedin: "https://www.linkedin.com/in/"
