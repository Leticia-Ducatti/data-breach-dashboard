import plotly.express as px

def plot_breaches_by_sector(df):
    setor_counts = df['Setor'].value_counts().reset_index()
    setor_counts.columns = ['Setor', 'count']
    fig = px.bar(
        setor_counts,
        x='Setor',
        y='count',
        title='Vazamentos por Setor'
    )
    return fig

def plot_breach_type_pie(df):
    tipo_counts = df['Tipo de Vazamento'].value_counts().reset_index()
    tipo_counts.columns = ['Tipo de Vazamento', 'count']
    fig = px.pie(
        tipo_counts,
        names='Tipo de Vazamento',
        values='count',
        title='Distribuição dos Tipos de Vazamento'
    )
    return fig