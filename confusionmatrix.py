def evaluatepredictions(y_pred, y_true):
    tp,tn, fp, fn, precision,recall, f1_score = 0,0,0,0,0,0,0
    try:
        for i in range(len(y_true)):
            if y_true[i] == 1 and y_pred[i] == 1:
                tp += 1
            elif y_true[i] == 0 and y_pred[i] == 1:
                fp += 1
            elif y_true[i] == 1 and y_pred[i] == 0:
                fn += 1
            else:
                tn += 1
    except ZeroDivisionError:
        print("no positives")
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*((precision * recall) / (precision + recall))
    return precision, recall, f1_score

def main():
    y_true = [1, 0, 1, 1, 0, 0, 1, 0, 0, 0]
    y_pred = [1, 0, 0, 1, 1, 0, 1, 0, 0, 1]
    precision,recall,f1_score = evaluatepredictions(y_pred, y_true)
    print(f"Precision: {precision}, Recall: {recall}, F1: {f1_score}")

if __name__ == "__main__":
    main()


