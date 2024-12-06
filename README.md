
# Lung Cancer Detection Using Machine Learning

This repository contains the implementation of a machine learning-based system for the early detection of lung cancer using computed tomography (CT) scan images. The project leverages various machine learning algorithms and preprocessing techniques to classify CT images as cancerous or non-cancerous.

---

## Project Overview

### Objective:
To develop a system that aids in the early detection of lung cancer by analyzing CT scan images, thereby improving patient outcomes.

### Features:
- **Data Acquisition**: Load and preprocess a CT scan dataset for training and testing.
- **Model Training**: Train multiple machine learning models including Random Forest, Decision Tree, Logistic Regression, SVM, and KNN.
- **Model Evaluation**: Assess model performance using metrics such as accuracy, precision, recall, and F1-score.
- **Best Model Selection**: Choose the best-performing model and deploy it.
- **User Interface**: Provide an intuitive interface using Streamlit for real-time predictions.

---

## Dataset

- **Source**: CT scan images of lungs sourced from Kaggle.
- **Size**: 2000 labeled images.
- **Classes**: Four classes, including different types of lung cancers and normal cases.

---

## Methodology

1. **Data Preprocessing**:
   - Resize images to 224x224.
   - Perform label encoding and data normalization.
   - Split data into training and testing sets.

2. **Dimensionality Reduction**:
   - Apply Principal Component Analysis (PCA) to reduce feature dimensions.

3. **Model Training**:
   - Train machine learning models and compare performance.
   - Models used:
     - Random Forest
     - Decision Tree
     - Logistic Regression
     - Support Vector Machine (SVM)
     - K-Nearest Neighbors (KNN)

4. **Evaluation**:
   - Generate classification reports and confusion matrices.
   - Visualize feature importance and model coefficients.

5. **Deployment**:
   - Deploy the selected model using a Streamlit-based user interface.

---

## Usage

- Upload a CT scan image via the Streamlit app.
- The app preprocesses the image and feeds it to the trained model.
- The predicted class and confidence scores are displayed.

---

## Results

- Achieved high accuracy using the **Random Forest Classifier**.
- Detailed evaluation metrics and confusion matrix are provided in the `results` folder.

---

## Challenges and Considerations

- **Data Privacy**: Ensure compliance with data protection regulations.
- **Ethical Concerns**: Mitigate algorithmic biases.
- **Scalability**: Optimize the system for large-scale deployment.

---

## Future Scope

- Integration of deep learning models for enhanced accuracy.
- Validation with larger datasets.
- Incorporation of clinical trials to test real-world effectiveness.

---

## Contributors

- Ari Nikhil Sai

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

Special thanks to:
- **Dr. Prashant Upadhyay** for guidance and support.
- Vignan's Foundation for Science, Technology & Research for providing resources.

