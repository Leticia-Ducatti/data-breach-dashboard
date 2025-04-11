from faker import Faker
import pandas as pd
import random

def generate_fake_breach_data(num_records=100):
    fake = Faker()
    data = {
        'Organização': [fake.company() for _ in range(num_records)],
        'Setor': [random.choice(['Financeiro', 'Saúde', 'Varejo', 'Tecnologia', 'Educação']) for _ in range(num_records)],
        'Data de Vazamento': [fake.date_between(start_date='-5y', end_date='today') for _ in range(num_records)],
        'Registros Afetados': [random.randint(1000, 1000000) for _ in range(num_records)],
        'Tipo de Vazamento': [random.choice(['Phishing', 'Malware', 'Ransomware', 'Insider', 'Dispositivo Perdido']) for _ in range(num_records)],
    }
    df = pd.DataFrame(data)
    return df