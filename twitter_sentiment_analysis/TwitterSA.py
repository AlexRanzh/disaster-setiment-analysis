from afinn import Afinn
import pandas as pd


def data_load():
    in_content_list = in_df.full_text.tolist()
    post_content_list = post_df.full_text.tolist()
    pre_content_list = pre_df.full_text.tolist()
    return in_content_list, post_content_list, pre_content_list


def sentiment_score(content_list):
    afinn = Afinn()
    score_list = list()
    for sentence in content_list:
        score_list.append(afinn.score(str(sentence)))
    return score_list


def sentiment_label(score_list):
    label_list = list()
    for score in score_list:
        if score > 0:
            label_list.append('positive')
        elif score < 0:
            label_list.append('negative')
        else:
            label_list.append('neutral')
    return label_list


def normalization(score_list):
    # normalize data from -5 to 5
    max_val = max(score_list)
    min_val = min(score_list)
    normalized_score_list = list()
    for score in score_list:
        if score > 0:
            norm_score = 5 * (score - 1.0) / (max_val - 1.0)
        elif score < 0:
            norm_score = 5 * (score - min_val) / (-1.0 - min_val) - 5
        else:
            norm_score = 0.0
        norm_round = round(norm_score, 1)
        normalized_score_list.append(norm_round)
    return normalized_score_list


def write_csv():
    in_df['score'] = in_sentiment_score
    in_df['normalized_score'] = normalized_in_score
    in_df['label'] = in_sentiment_label
    in_df.to_csv('in_sentiment_result.csv', index=False)

    post_df['score'] = post_sentiment_score
    post_df['normalized_score'] = normalized_post_score
    post_df['label'] = post_sentiment_label
    post_df.to_csv('post_sentiment_result.csv', index=False)

    pre_df['score'] = pre_sentiment_score
    pre_df['normalized_score'] = normalized_pre_score
    pre_df['label'] = pre_sentiment_label
    pre_df.to_csv('pre_sentiment_result.csv', index=False)


if __name__ == '__main__':
    # read data
    in_df = pd.read_csv(r'./twitter_data_processed/processed_in_h.csv')
    post_df = pd.read_csv(r'./twitter_data_processed/processed_post_h.csv')
    pre_df = pd.read_csv(r'./twitter_data_processed/processed_pre_h.csv')

    in_content_list, post_content_list, pre_content_list = data_load()

    # get the score
    in_sentiment_score = sentiment_score(in_content_list)
    post_sentiment_score = sentiment_score(post_content_list)
    pre_sentiment_score = sentiment_score(pre_content_list)

    # get the label
    in_sentiment_label = sentiment_label(in_sentiment_score)
    post_sentiment_label = sentiment_label(post_sentiment_score)
    pre_sentiment_label = sentiment_label(pre_sentiment_score)

    # normalize the score
    normalized_in_score = normalization(in_sentiment_score)
    normalized_post_score = normalization(post_sentiment_score)
    normalized_pre_score = normalization(pre_sentiment_score)

    # write the csv file separately
    write_csv()
