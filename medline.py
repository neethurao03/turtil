class MedicalAid:
    def __init__(self):
        self.patients = []
        self.volunteers = []
        self.disease_database = {
            "fever": "Possible flu or viral infection",
            "cough": "Possible cold or respiratory infection",
            "chest pain": "Consult a doctor, could be heart-related",
            "headache": "May be due to stress, migraine, or dehydration",
        }

    def add_patient(self, name, symptoms, economic_status):
        diagnosis = self.diagnose(symptoms)
        patient = {
            "name": name,
            "symptoms": symptoms,
            "diagnosis": diagnosis,
            "economic_status": economic_status,
            "funding_required": economic_status.lower() == "poor",
        }
        self.patients.append(patient)
        return patient

    def diagnose(self, symptoms):
        for symptom in symptoms:
            if symptom in self.disease_database:
                return self.disease_database[symptom]
        return "Unknown disease, consult a doctor"

    def add_volunteer(self, name, contact):
        self.volunteers.append({"name": name, "contact": contact})
        return f"Volunteer {name} added."

    def get_patients_needing_funding(self):
        return [p for p in self.patients if p["funding_required"]]

    def get_all_patients(self):
        return self.patients


# Example Usage
healthcare = MedicalAid()

# Adding patients
healthcare.add_patient("Ravi", ["fever", "cough"], "poor")
healthcare.add_patient("Sita", ["headache"], "middle class")

# Adding volunteers
healthcare.add_volunteer("Dr. Sharma", "dr.sharma@example.com")

# Displaying patients needing funding
print("\nPatients Needing Funding:")
for patient in healthcare.get_patients_needing_funding():
    print(patient)

# Displaying all patients
print("\nAll Patients:")
for patient in healthcare.get_all_patients():
    print(patient)