import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to categorize BMI with obesity levels
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif 30 <= bmi < 34.9:
        return "Obesity Class 1"
    elif 35 <= bmi < 39.9:
        return "Obesity Class 2"
    else:
        return "Obesity Class 3 (Severe)"

# Function to display a detailed diet plan
def suggest_diet_plan(category, conditions):
    diet = ""
    if category == "Underweight":
        diet += (
            "- **Calorie-dense foods**: Nuts, seeds, avocado, and whole grains.\n"
            "- **Frequent meals**: Eat every 3-4 hours with snacks.\n"
            "- **Healthy fats**: Olive oil, peanut butter, and fatty fish.\n"
        )
    elif category == "Normal weight":
        diet += (
            "- **Balanced diet**: Vegetables, lean protein, and complex carbs.\n"
            "- **Portion control**: Avoid overeating.\n"
            "- **Hydration**: Drink at least 2-3 liters of water daily.\n"
        )
    elif category == "Overweight":
        diet += (
            "- **Calorie deficit**: Reduce daily intake by 500-700 calories.\n"
            "- **Increase fiber intake**: Vegetables, fruits, and oats.\n"
            "- **Avoid sugary foods**: Cut down on refined sugars and carbs.\n"
        )
    else:
        diet += (
            "- **Low-carb diet**: Avoid starchy foods like rice and potatoes.\n"
            "- **Medical supervision**: Consult a dietitian.\n"
            "- **Hydration**: Drink water 30 minutes before meals.\n"
        )

    if "PCOS" in conditions:
        diet += "\n**PCOS Advice:** Focus on anti-inflammatory foods and strength training.\n"
    if "Diabetes" in conditions:
        diet += "\n**Diabetes Advice:** Monitor carbs, avoid sugars, and focus on low-GI foods.\n"
    if "Hypertension" in conditions:
        diet += "\n**Hypertension Advice:** Follow a DASH diet with reduced salt intake.\n"

    return diet

# Function to suggest an exercise plan
def suggest_exercise_plan(category):
    if category in ["Underweight", "Normal weight"]:
        return "30 minutes of moderate exercise like walking or cycling, 2-3 times a week."
    elif category == "Overweight":
        return "Cardio workouts like swimming or running, plus strength training 3-4 times a week."
    else:
        return (
            "Low-impact activities like yoga or water aerobics. Consult a trainer for guided workouts."
        )

# Streamlit App
def main():
    st.title("BMI Calculator")
    st.subheader("Created by Ruba Fareed")

    # Collecting user information
    age = st.number_input("Enter your age", min_value=1, max_value=120, value=25)
    gender = st.selectbox("Select your gender", ["Man", "Woman", "Child"])

    if gender == "Woman":
        pregnant = st.radio("Are you pregnant?", ["Yes", "No"])
        if pregnant == "Yes":
            st.warning("Pregnancy detected. Consult your doctor for specific advice.")

    # Health conditions
    st.write("Select any health conditions you have:")
    conditions = []
    if st.checkbox("Diabetes"):
        conditions.append("Diabetes")
    if st.checkbox("Hypertension"):
        conditions.append("Hypertension")
    if st.checkbox("Hypotension"):
        conditions.append("Hypotension")
    if st.checkbox("PCOS (Polycystic Ovary Syndrome)"):
        conditions.append("PCOS")

    # Height and weight inputs
    height = st.number_input("Enter your height in meters", min_value=0.5, max_value=2.5, value=1.7)
    weight = st.number_input("Enter your weight in kilograms", min_value=10.0, max_value=300.0, value=70.0)

    if st.button("Calculate BMI"):
        # Calculate and display BMI
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)

        st.success(f"Your BMI is: {bmi:.2f} ({category})")

        # Display diet and exercise recommendations
        st.subheader("Diet Recommendations")
        st.markdown(suggest_diet_plan(category, conditions))

        st.subheader("Exercise Recommendations")
        st.write(suggest_exercise_plan(category))

# Run the app
if __name__ == "__main__":
    main()
