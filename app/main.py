import joblib
import numpy as np

LABELS = {27: 'Human Resources', 18: 'Customer Service', 23: 'Product', 19: 'Software Development',
          30: 'Sales', 32: 'Writing', 33: 'Business', 24: 'Data', 28: 'Marketing', 25: 'DevOps/sysadmin',
          21: 'Design', 26: 'Finance/ Legal', 29: 'QA'}

FALLBACK = (22, 'All Others')


def load_model(model_filename='../Models/model.pkl'):
    """
    Loads and returns the pretrained model
    """
    model = joblib.load(model_filename)
    return model


def predict(input_data, model, seuil_min=0.4, seuil_max=0.7):
    # find the max probability
    probabilities = np.max(model.predict_proba(input_data), axis=1)
    ids = model.predict(input_data)

    response = []

    for k in range(len(input_data)):
        proba = probabilities[k]

        if proba < seuil_min:
            proba = False

        ID = int(ids[k]) if proba else FALLBACK[0]

        response.append(
            {
                "proba": proba,
                "id": ID,
                "name": LABELS[ID] if proba else FALLBACK[1],
                "need_check": proba < seuil_max if proba else False,
            }
        )

    return response


if __name__ == "__main__":
    model = load_model()
    job_titles = ['Software Engineer - Infrastructure, Reliability', 'Product Manager']
    response = predict(job_titles, model, 0.4, 0.7)
    print(response)
