import streamlit as st
import pandas as pd
import joblib
from sklearn.impute import SimpleImputer
import yaml
import json
# Load the model
model = joblib.load('model/model.joblib')

# Function to convert PType labels
def convert_ptype_label(label):
    if label == 'L':
        return 1
    elif label == 'M':
        return 2
    elif label == 'H':
        return 0

def predict_tool_wear(inputs):
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(inputs, index=[0])  # Create a single-row DataFrame
    
    # Impute missing values
    imputer = SimpleImputer(strategy='mean')
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    
    # Convert PType label (unchanged)
    #df_imputed['PType'] = convert_ptype_label(df_imputed['PType'])

    # Make the prediction
    prediction = model.predict(df_imputed)[0]

    return prediction

# Main function
def main():
    # Set page title and page layout
    st.set_page_config(page_title='Machine Wear Prediction', layout='wide')

    # Load the params.yaml file
    with open('params.yaml', 'r') as file:
        params = yaml.load(file, Loader=yaml.FullLoader)

    # Create a sidebar for user inputs
    st.sidebar.title('Input Parameters')
    air_temp = st.sidebar.slider('Air Temperature (K)', 0, 400, st.session_state.get('air_temp', 300))
    process_temp = st.sidebar.slider('Process Temperature (K)', 0, 400, st.session_state.get('process_temp', 300))
    rotational_speed = st.sidebar.slider('Rotational Speed (rpm)', 0, 4000, st.session_state.get('rotational_speed', 2000))
    torque = st.sidebar.slider('Torque (Nm)', 0, 100, st.session_state.get('torque', 50))
    tool_wear = st.sidebar.slider('Tool Wear (min)', 0, 200, st.session_state.get('tool_wear', 100))
    ptype = st.sidebar.selectbox('PType', ['Low', 'Medium', 'High'], index=st.session_state.get('ptype', 0))

    # Create a dictionary of user inputs
    ptype_mapping = {'Low': 1, 'Medium': 2, 'High': 0}
    inputs = {
        'Air temperature [K]': air_temp,
        'Process temperature [K]': process_temp,
        'Rotational speed [rpm]': rotational_speed,
        'Torque [Nm]': torque,
        'Tool wear [min]': tool_wear,
        'TWF': 0,
        'HDF': 0,
        'PWF': 0,
        'OSF': 0,
        'RNF': 0,
        'PType': ptype_mapping[ptype]
    }

    # Predict tool wear
    prediction = predict_tool_wear(inputs)

    # Display the prediction in the main section
    st.title('Machine Wear Prediction')
    if prediction == 0:
        st.markdown(f"<p style='font-size: 30px; color: green;'>Machine is in good condition</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p style='font-size: 30px; color: red;'>Machine is going to fail soon</p>", unsafe_allow_html=True)

    # Add a section to update the params.yaml file
    st.sidebar.title('Update Hyper-Parameters')
    max_iter = st.sidebar.number_input('max_iter', value=params['LogisticRegression']['max_iter'], min_value=1, step=1)
    penalty = st.sidebar.selectbox('penalty', ['l1', 'l2', 'elasticnet'], index=['l1', 'l2', 'elasticnet'].index(params['LogisticRegression']['penalty']))
    solver = st.sidebar.selectbox('solver', ['lbfgs', 'saga', 'newton-cg'], index=['lbfgs', 'saga', 'newton-cg'].index(params['LogisticRegression']['solver']))
    l1_ratio = st.sidebar.number_input('l1_ratio', value=params['LogisticRegression']['l1_ratio'], min_value=0.0, max_value=1.0, step=0.1)

    # Add a button to run the main.py script and update the params.yaml file
    if st.sidebar.button('Train Model'):

        # Update the params.yaml file
        params['LogisticRegression']['max_iter'] = max_iter
        params['LogisticRegression']['penalty'] = penalty
        params['LogisticRegression']['solver'] = solver
        params['LogisticRegression']['l1_ratio'] = l1_ratio

        with open('params.yaml', 'w') as file:
            yaml.dump(params, file)

        # Update the session state
        st.session_state['air_temp'] = air_temp
        st.session_state['process_temp'] = process_temp
        st.session_state['rotational_speed'] = rotational_speed
        st.session_state['torque'] = torque
        st.session_state['tool_wear'] = tool_wear
        st.session_state['ptype'] = ['Low', 'Medium', 'High'].index(ptype)

        # Run the main.py script
        import run
        run.main()
        try:
            with open('model/metrics.json', 'r') as file:
                metrics = json.load(file)
            st.write("Model evaluation metrics:")
            st.write(metrics)
        except FileNotFoundError:
            st.write("Error: metrics.json file not found.")
        except Exception as e:
            st.write(f"Error: {e}")



# Run the app
if __name__ == '__main__':
    main()