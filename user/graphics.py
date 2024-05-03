import io

import matplotlib.pyplot as plt
import base64
from io import BytesIO
import matplotlib.patches as mpatches
import numpy as np
# views.py
def hybrid_metrics():
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']

    values = [0.8, 0.78, 0.78, 0.78]

    # Создайте график
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(metrics, values, color=['blue', 'green', 'orange', 'red'])
    ax.set_ylabel('Values')

    # Сохраните график в формате PNG
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Преобразуйте изображение в строку base64
    graphic = base64.b64encode(image_png).decode('utf-8')
    image_tag = f'<img src="data:image/png;base64,{graphic}">'
    print('f2', image_tag)

    return image_tag

def plot():
    cosine_similarity = [1.000, 0.997, 0.982, 0.975, 0.998, 0.990, 0.985, 0.979, 0.999, 0.973,
                         0.987, 0.978, 0.966, 0.991, 0.970, 0.994, 0.968, 0.983, 0.997, 0.976]
    success_failure_category = [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
    colors = ['green' if category == 1 else 'red' for category in success_failure_category]

    # Создайте график с более плотной последовательностью для гладкости
    x_smooth = np.linspace(min(cosine_similarity), max(cosine_similarity), 100)
    y_smooth = np.interp(x_smooth, cosine_similarity, success_failure_category)

    fig, ax = plt.subplots()
    ax.plot(x_smooth, y_smooth, color='gray', linestyle='--', label='Smoothed Line')
    ax.scatter(cosine_similarity, success_failure_category, c=colors)
    ax.set_xlabel('Cosine Similarity')
    ax.set_ylabel('Category of Success/Failure')

    # Сохраните график в формате PNG
    legend_labels = {1: 'Success', 0: 'Failure'}
    handles = [mpatches.Patch(color=color, label=label) for color, label in zip(['green', 'red'], legend_labels.values())]
    ax.legend(handles=handles)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Преобразуйте изображение в строку base64
    graphic = base64.b64encode(image_png).decode('utf-8')
    image_tag = f'<img src="data:image/png;base64,{graphic}">'
    print('ff', image_tag)

    return image_tag


# views.py
def comparison_metrics():
    # Ваши данные для графика 3
    methods = ['Hybrid method', 'Collaborative filtering', 'Naive Bayes']
    accuracy = [85, 80, 75]
    precision = [88, 82, 79]
    recall = [90, 85, 78]
    f1_score = [89, 84, 80]

    # Создайте график
    fig, ax = plt.subplots()
    ax.plot(methods, accuracy, label='Accuracy')
    ax.plot(methods, precision, label='Precision')
    ax.plot(methods, recall, label='Recall')
    ax.plot(methods, f1_score, label='F1-Score')
    ax.set_ylabel('Values')
    ax.legend()

    # Сохраните график в формате PNG
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Преобразуйте изображение в строку base64
    graphic = base64.b64encode(image_png).decode('utf-8')
    image_tag = f'<img src="data:image/png;base64,{graphic}">'

    return image_tag




def plot_to_base64(figure):
    buf = io.BytesIO()
    figure.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

def graph1(request):
    population_size = list(range(1, 11))
    min_selectivity = 0.5
    max_selectivity = 1.0

    fig, ax = plt.subplots(figsize=(6, 4), dpi=80)


    plt.plot(population_size, [min_selectivity] * len(population_size), label='Min Selectivity')
    plt.plot(population_size, [max_selectivity] * len(population_size), label='Max Selectivity')
    plt.xlabel('Population Size')
    plt.ylabel('Selectivity')
    plt.legend()
    plt.title('Graph 1')

    graph_base64 = plot_to_base64(plt)
    plt.close()

    return graph_base64


def graph2(request):
    population_size = 10
    initial_population = [0.8, 0.6, 0.9, 0.7]
    final_population = [0.85, 0.65, 0.92, 0.68]

    fig, ax = plt.subplots(figsize=(6, 4), dpi=80)

    ax.plot(range(len(initial_population)), initial_population, label='Initial Population')
    ax.plot(range(len(final_population)), final_population, label='Final Population')
    ax.set_xlabel('Individuals')
    ax.set_ylabel('Population Values')
    ax.legend()
    ax.set_title('Graph 2')

    graph_base64 = plot_to_base64(fig)
    plt.close()

    return graph_base64


def graph3(request):
    iterations = list(range(1, 11))
    selectivity_values = [0.8, 0.85, 0.9, 0.92, 0.95, 0.97, 0.98, 0.99, 0.995, 1.0]

    fig, ax = plt.subplots(figsize=(6, 4), dpi=80)

    ax.plot(iterations, selectivity_values, marker='o')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Selectivity Values')
    ax.set_title('Graph 3')

    graph_base64 = plot_to_base64(fig)
    plt.close()

    return graph_base64


# ...

# ...

# ...

# ...

def graph4(request):
    iterations_repeat = list(range(1, 6))
    selectivity_values_repeat = [0.995, 0.997, 0.999, 1.0, 1.001]
    iterations = list(range(1, 11))
    initial_selectivity = [0.8, 0.82, 0.79, 0.83, 0.85, 0.84, 0.81, 0.86, 0.82, 0.85]
    final_selectivity = [0.82, 0.84, 0.88, 0.86, 0.9, 0.92, 0.91, 0.93, 0.94, 0.95]

    fig, ax = plt.subplots(figsize=(6, 4), dpi=80)

    ax.plot(iterations_repeat, selectivity_values_repeat, label='Selectivity Repeat', marker='o')
    for i in range(len(initial_selectivity)):
        ax.plot(iterations, [initial_selectivity[i]] * len(iterations), linestyle='dashed', label=f'Membrane {i + 1}')
        ax.plot(iterations, [final_selectivity[i]] * len(iterations), linestyle='dashed')

    ax.set_xlabel('Iterations')
    ax.set_ylabel('Selectivity Values')
    ax.legend()
    ax.set_title('Graph 4')

    graph_base64 = plot_to_base64(fig)
    plt.close()

    return graph_base64


# ...

def graph5(request):
    iterations = list(range(1, 4))
    membrane_values = [
        [0.75, 0.82, 0.71, 0.79],
        [0.76, 0.83, 0.73, 0.81],
        [0.78, 0.85, 0.75, 0.82]
    ]

    fig, ax = plt.subplots(figsize=(6, 4), dpi=80)

    for i in range(len(membrane_values[0])):
        ax.plot(iterations, [membrane_values[j][i] for j in range(len(iterations))], marker='o', label=f'Membrane {i + 1}')

    ax.set_xlabel('Iterations')
    ax.set_ylabel('Selectivity Values')
    ax.legend()
    ax.set_title('Graph 5')

    graph_base64 = plot_to_base64(fig)
    plt.close()

    return graph_base64

# ...

def graph6(request):
    iterations = list(range(10))
    optimal_membrane_values = [0.75, 0.78, 0.82, 0.85, 0.89, 0.88, 0.90, 0.91, 0.89, 0.92]

    fig, ax = plt.subplots(figsize=(6, 4), dpi=80)

    ax.plot(iterations, optimal_membrane_values, marker='o')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Optimal Membrane Values')
    ax.set_title('Graph 6')

    graph_base64 = plot_to_base64(fig)
    plt.close()

    return graph_base64



