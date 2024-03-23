def main():
    print("¡Bienvenido al diagnóstico de diabetes!")
    print("Por favor, responde a las siguientes preguntas:")
    
    # edad
    age = int(input("¿Cuál es tu edad? "))
    
    # peso y la altura
    weight = float(input("¿Cuál es tu peso en kg? "))
    height = float(input("¿Cuál es tu altura en metros? "))
    
    bmi = calculate_bmi(weight, height)
    
    family_history = input("¿Hay antecedentes de diabetes en tu familia? (Sí/No) ").lower()
    
    physical_activity = input("¿Realizas actividad física regularmente? (Sí/No) ").lower()
    
    blood_pressure = input("¿Tienes la presión arterial alta? (Sí/No) ").lower()
    
    fasting_glucose = float(input("¿Cuál es tu nivel de glucosa en ayunas? "))
    
    sugar_consumption = input("¿Consume mucha azúcar en tu dieta? (Sí/No) ").lower()
    
    probability, overweight_due_to_sugar, overweight = calculate_diabetes_probability(age, bmi, family_history, physical_activity, blood_pressure, fasting_glucose, sugar_consumption)
    

    print("\nBasado en tus respuestas, la probabilidad de que tengas diabetes es del {:.2f}%.".format(probability * 100))
    if overweight_due_to_sugar:
        print("También es probable que tengas sobrepeso debido al consumo de azúcar.")
    if overweight:
        print("También tienes sobrepeso. Te recomendamos consultar a un médico para obtener asesoramiento adecuado.")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def calculate_diabetes_probability(age, bmi, family_history, physical_activity, blood_pressure, fasting_glucose, sugar_consumption):
    probability = 0.1
    overweight_due_to_sugar = False
    overweight = False
    
    if age >= 45:
        probability += 0.15
    elif age >= 30:
        probability += 0.1
    
    if bmi >= 30:
        probability += 0.15
        overweight = True
    elif bmi >= 25:
        probability += 0.1
        overweight = True
    
    if family_history == "sí":
        probability += 0.1
    
    if physical_activity == "no":
        probability += 0.1
    
    if blood_pressure == "sí":
        probability += 0.1
    
    if fasting_glucose >= 126:
        probability += 0.15
    elif fasting_glucose >= 100:
        probability += 0.1
    
    if sugar_consumption == "sí" and bmi >= 25:
        overweight_due_to_sugar = True
    
    return min(1.0, probability), overweight_due_to_sugar, overweight  


if __name__ == "__main__":
    main()
