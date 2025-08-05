class ExcelReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_excel(self):
        import pandas as pd
        self.data = pd.read_excel(self.file_path)

    def parse_forms(self):
        if self.data is None:
            raise ValueError("No data has been read. Please call read_excel() first.")
        
        # Assuming the forms have specific columns to extract
        forms_data = []
        for index, row in self.data.iterrows():
            form_info = {
                'name': row.get('Name'),
                'email': row.get('Email'),
                'submission_date': row.get('Submission Date'),
                # Add more fields as necessary
            }
            forms_data.append(form_info)
        
        return forms_data