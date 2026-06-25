# load the saved model back into the memory (for demonstration)
import joblib
import pandas as pd


# To this:
model_filename = r'c:\Users\Admin\Downloads\My_work\customer_churn\notebook\customer_churn_model.joblib'


loaded_model = joblib.load(model_filename)

# create a sample input for prediction
sample_input = pd.DataFrame({
    'tenure': [12],
    'monthly_charges': [70.0],
    'total_charges': [840.0],
    'contract': ['Month-to-month'],
    'online_security': ['No'],
    'support_calls': [2],
    'payment_method': ['Credit'],
    'internet_service': ['Fiber'],
    'tech_support': ['No'],
})

predicted_output = loaded_model.predict(sample_input)
print(f'Predicted churn for the sample input: {predicted_output[0]}')
