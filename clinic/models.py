"""The Patient class — the OOP heart of the project.

Two OOP ideas to demonstrate (only two, on purpose):
1. ENCAPSULATION — consultation_fee guarded by @property (Module 6).
2. FACTORY CLASSMETHOD — Patient.from_csv_row() builds a validated
   Patient from a messy CSV row (Module 5 + Module 8 together).
"""

from clinic import validators


class Patient:
    """One validated patient visit record."""

    def __init__(self, patient_id: str, name: str, age: int,
                 department: str, consultation_fee: float, visit_date: str):
        # TODO 5: store all six values on self.
        # Assign consultation_fee normally — it must go through the setter.
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.department = department
        self.consultation_fee = consultation_fee
        self.visit_date = visit_date
    # ----- encapsulation: a guarded attribute -----
    @property
    def consultation_fee(self) -> float:
        # TODO 6: return the private attribute self._consultation_fee
        return self._consultation_fee

    @consultation_fee.setter
    def consultation_fee(self, value: float):
        # TODO 7: raise ValueError if value < 0, else store it
        # in self._consultation_fee
        if value < 0:
         raise ValueError("Consultation fee cannot be negative")
        self._consultation_fee = value

    # ----- factory: build a Patient from one raw CSV row (a dict) -----
    @classmethod
    def from_csv_row(cls, row: dict) -> "Patient":

        """Validate and convert one csv.DictReader row into a Patient.

        Use the validators module for name / age / department / fee;
        .strip() is enough for patient_id and visit_date.
        Let InvalidRecordError bubble up to the caller (storage handles it).
        """
        # TODO 8: return cls(...) with all six cleaned values
        return cls(
            row["patient_id"].strip(),
            validators.clean_name(row["name"]),
            validators.parse_age(row["age"]),
            validators.clean_department(row["department"]),
            validators.parse_fee(row["consultation_fee"]),
            row["visit_date"].strip(),
        )

    def to_dict(self) -> dict:
        """Return a plain dict — the shape JSON and CSV writers need."""
        # TODO 9: six keys matching the CSV header names
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": str(self.age),
            "department": self.department,
            "consultation_fee": self.consultation_fee,
            "visit_date": self.visit_date,
        }
    def __repr__(self) -> str:
        return f"Patient({self.patient_id}, {self.name}, {self.department})"


if __name__ == "__main__":
    # Self-test (Module 7 pattern) — works once TODOs 5-7 are done
    demo = Patient("P999", "Test Person", 30, "General", 500.0, "2026-08-12")
    print("Self-test:", demo)
