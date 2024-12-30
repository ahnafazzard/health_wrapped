So I tested [health_records](health_records.py) with sample data in [sample_data/export.json](sample_data/export.json) (which is created from [zip_extract](zip_extract.py) using [sample_data/export.zip](sample_data/export.zip))

Here are some metrics we have so far


```json
{
  "get_total_steps_for_year_2024": "3363195 step(s)",
  "get_total_distance_for_year_2024": "2595.92 km",
  "get_total_calories_for_year_2024": "136783.57 Cal",
  "get_average_vo2max_2024": "38.79 mL/min·kg",
  "get_stats_by_week_2024": [
    {
      "week": 1,
      "total_steps": 16989,
      "start_date": "2024-01-01",
      "end_date": "2024-01-07"
    },
    {
      "week": 2,
      "total_steps": 19447,
      "start_date": "2024-01-08",
      "end_date": "2024-01-14"
    },
    {
      "week": 3,
      "total_steps": 21266,
      "start_date": "2024-01-15",
      "end_date": "2024-01-21"
    },
    {
      "week": 4,
      "total_steps": 23132,
      "start_date": "2024-01-22",
      "end_date": "2024-01-28"
    },
    {
      "week": 5,
      "total_steps": 26018,
      "start_date": "2024-01-29",
      "end_date": "2024-02-04"
    },
    {
      "week": 6,
      "total_steps": 32027,
      "start_date": "2024-02-05",
      "end_date": "2024-02-11"
    },
    {
      "week": 7,
      "total_steps": 25676,
      "start_date": "2024-02-12",
      "end_date": "2024-02-18"
    },
    {
      "week": 8,
      "total_steps": 29579,
      "start_date": "2024-02-19",
      "end_date": "2024-02-25"
    },
    {
      "week": 9,
      "total_steps": 21571,
      "start_date": "2024-02-26",
      "end_date": "2024-03-04"
    },
    {
      "week": 10,
      "total_steps": 27707,
      "start_date": "2024-03-04",
      "end_date": "2024-03-10"
    },
    {
      "week": 11,
      "total_steps": 21210,
      "start_date": "2024-03-11",
      "end_date": "2024-03-17"
    },
    {
      "week": 12,
      "total_steps": 26838,
      "start_date": "2024-03-18",
      "end_date": "2024-03-24"
    },
    {
      "week": 13,
      "total_steps": 28755,
      "start_date": "2024-03-25",
      "end_date": "2024-03-31"
    },
    {
      "week": 14,
      "total_steps": 28216,
      "start_date": "2024-04-01",
      "end_date": "2024-04-07"
    },
    {
      "week": 15,
      "total_steps": 27461,
      "start_date": "2024-04-08",
      "end_date": "2024-04-14"
    },
    {
      "week": 16,
      "total_steps": 24222,
      "start_date": "2024-04-15",
      "end_date": "2024-04-21"
    },
    {
      "week": 17,
      "total_steps": 28326,
      "start_date": "2024-04-22",
      "end_date": "2024-04-28"
    },
    {
      "week": 18,
      "total_steps": 42908,
      "start_date": "2024-04-29",
      "end_date": "2024-05-05"
    },
    {
      "week": 19,
      "total_steps": 58281,
      "start_date": "2024-05-06",
      "end_date": "2024-05-12"
    },
    {
      "week": 20,
      "total_steps": 88708,
      "start_date": "2024-05-13",
      "end_date": "2024-05-19"
    },
    {
      "week": 21,
      "total_steps": 128658,
      "start_date": "2024-05-20",
      "end_date": "2024-05-26"
    },
    {
      "week": 22,
      "total_steps": 104519,
      "start_date": "2024-05-27",
      "end_date": "2024-06-02"
    },
    {
      "week": 23,
      "total_steps": 101651,
      "start_date": "2024-06-03",
      "end_date": "2024-06-09"
    },
    {
      "week": 24,
      "total_steps": 82028,
      "start_date": "2024-06-10",
      "end_date": "2024-06-16"
    },
    {
      "week": 25,
      "total_steps": 118199,
      "start_date": "2024-06-17",
      "end_date": "2024-06-23"
    },
    {
      "week": 26,
      "total_steps": 106218,
      "start_date": "2024-06-24",
      "end_date": "2024-06-30"
    },
    {
      "week": 27,
      "total_steps": 114042,
      "start_date": "2024-07-01",
      "end_date": "2024-07-07"
    },
    {
      "week": 28,
      "total_steps": 94561,
      "start_date": "2024-07-08",
      "end_date": "2024-07-14"
    },
    {
      "week": 29,
      "total_steps": 104672,
      "start_date": "2024-07-15",
      "end_date": "2024-07-21"
    },
    {
      "week": 30,
      "total_steps": 72050,
      "start_date": "2024-07-22",
      "end_date": "2024-07-28"
    },
    {
      "week": 31,
      "total_steps": 85866,
      "start_date": "2024-07-29",
      "end_date": "2024-08-04"
    },
    {
      "week": 32,
      "total_steps": 112336,
      "start_date": "2024-08-05",
      "end_date": "2024-08-11"
    },
    {
      "week": 33,
      "total_steps": 95512,
      "start_date": "2024-08-12",
      "end_date": "2024-08-18"
    },
    {
      "week": 34,
      "total_steps": 114020,
      "start_date": "2024-08-19",
      "end_date": "2024-08-25"
    },
    {
      "week": 35,
      "total_steps": 79997,
      "start_date": "2024-08-26",
      "end_date": "2024-09-01"
    },
    {
      "week": 36,
      "total_steps": 118371,
      "start_date": "2024-09-02",
      "end_date": "2024-09-08"
    },
    {
      "week": 37,
      "total_steps": 70627,
      "start_date": "2024-09-09",
      "end_date": "2024-09-16"
    },
    {
      "week": 38,
      "total_steps": 81921,
      "start_date": "2024-09-16",
      "end_date": "2024-09-22"
    },
    {
      "week": 39,
      "total_steps": 65983,
      "start_date": "2024-09-23",
      "end_date": "2024-09-29"
    },
    {
      "week": 40,
      "total_steps": 61595,
      "start_date": "2024-09-30",
      "end_date": "2024-10-06"
    },
    {
      "week": 41,
      "total_steps": 67642,
      "start_date": "2024-10-07",
      "end_date": "2024-10-13"
    },
    {
      "week": 42,
      "total_steps": 47446,
      "start_date": "2024-10-14",
      "end_date": "2024-10-20"
    },
    {
      "week": 43,
      "total_steps": 73059,
      "start_date": "2024-10-21",
      "end_date": "2024-10-27"
    },
    {
      "week": 44,
      "total_steps": 50418,
      "start_date": "2024-10-28",
      "end_date": "2024-11-03"
    },
    {
      "week": 45,
      "total_steps": 73406,
      "start_date": "2024-11-04",
      "end_date": "2024-11-10"
    },
    {
      "week": 46,
      "total_steps": 83110,
      "start_date": "2024-11-11",
      "end_date": "2024-11-18"
    },
    {
      "week": 47,
      "total_steps": 57931,
      "start_date": "2024-11-18",
      "end_date": "2024-11-24"
    },
    {
      "week": 48,
      "total_steps": 65808,
      "start_date": "2024-11-25",
      "end_date": "2024-12-01"
    },
    {
      "week": 49,
      "total_steps": 74545,
      "start_date": "2024-12-02",
      "end_date": "2024-12-08"
    },
    {
      "week": 50,
      "total_steps": 117366,
      "start_date": "2024-12-09",
      "end_date": "2024-12-15"
    },
    {
      "week": 51,
      "total_steps": 66465,
      "start_date": "2024-12-16",
      "end_date": "2024-12-22"
    },
    {
      "week": 52,
      "total_steps": 54836,
      "start_date": "2024-12-23",
      "end_date": "2024-12-28"
    }
  ],
  "get_best_week_2024": {
    "week": 21,
    "total_steps": 128658,
    "start_date": "2024-05-20",
    "end_date": "2024-05-26"
  }
}
```

I also tested [workout_records](workout_records.py), heres some metrics we have

```json
{
  "total_workout_calories_2024": "70137.59 Cal",
  "workout_stats_by_type_2024": {
    "Cycling": {
      "count": 7,
      "total_duration": 242.28,
      "total_calories": 821.4,
      "avg_heart_rate": 125.75
    },
    "Elliptical": {
      "count": 8,
      "total_duration": 180.8,
      "total_calories": 2042.22,
      "avg_heart_rate": 149.3
    },
    "FunctionalStrengthTraining": {
      "count": 4,
      "total_duration": 212.93,
      "total_calories": 1272.47,
      "avg_heart_rate": 112.8
    },
    "Golf": {
      "count": 3,
      "total_duration": 93.2,
      "total_calories": 163.95,
      "avg_heart_rate": 89.29
    },
    "HighIntensityIntervalTraining": {
      "count": 1,
      "total_duration": 9.68,
      "total_calories": 109.68,
      "avg_heart_rate": 136.98
    },
    "Hiking": {
      "count": 3,
      "total_duration": 335.93,
      "total_calories": 1335.04,
      "avg_heart_rate": 122.47
    },
    "PaddleSports": {
      "count": 1,
      "total_duration": 97.16,
      "total_calories": 478.77,
      "avg_heart_rate": 104.74
    },
    "Pickleball": {
      "count": 32,
      "total_duration": 2441.64,
      "total_calories": 27515.57,
      "avg_heart_rate": 142.32
    },
    "Running": {
      "count": 1,
      "total_duration": 8.87,
      "total_calories": 43.18,
      "avg_heart_rate": 108.67
    },
    "Tennis": {
      "count": 2,
      "total_duration": 125.01,
      "total_calories": 1201.82,
      "avg_heart_rate": 127.14
    },
    "TraditionalStrengthTraining": {
      "count": 42,
      "total_duration": 1916.2,
      "total_calories": 12364.03,
      "avg_heart_rate": 113.56
    },
    "Walking": {
      "count": 122,
      "total_duration": 4739.53,
      "total_calories": 22789.45,
      "avg_heart_rate": 114.04
    }
  },
  "highest_calorie_activity_2024": {
    "Pickleball": {
      "average_calories": 859.86,
      "total_calories": 27515.57,
      "workout_count": 32
    }
  },
  "most_frequent_workout_2024": {
    "Walking": 122
  },
  "peak_calorie_weeks_2024": [
    {
      "week": 27,
      "total_calories": 4646.1151,
      "workout_count": 8,
      "start_date": "2024-07-01",
      "end_date": "2024-07-07"
    },
    {
      "week": 23,
      "total_calories": 4203.544,
      "workout_count": 13,
      "start_date": "2024-06-03",
      "end_date": "2024-06-09"
    },
    {
      "week": 28,
      "total_calories": 4089.5899,
      "workout_count": 7,
      "start_date": "2024-07-08",
      "end_date": "2024-07-14"
    },
    {
      "week": 29,
      "total_calories": 4072.0961,
      "workout_count": 9,
      "start_date": "2024-07-15",
      "end_date": "2024-07-21"
    },
    {
      "week": 24,
      "total_calories": 3585.0856000000003,
      "workout_count": 9,
      "start_date": "2024-06-10",
      "end_date": "2024-06-16"
    },
    {
      "week": 22,
      "total_calories": 3336.2601,
      "workout_count": 12,
      "start_date": "2024-05-27",
      "end_date": "2024-06-02"
    },
    {
      "week": 33,
      "total_calories": 3212.9824000000003,
      "workout_count": 9,
      "start_date": "2024-08-12",
      "end_date": "2024-08-18"
    },
    {
      "week": 48,
      "total_calories": 3187.9254,
      "workout_count": 13,
      "start_date": "2024-11-25",
      "end_date": "2024-12-01"
    },
    {
      "week": 21,
      "total_calories": 3136.8214000000003,
      "workout_count": 9,
      "start_date": "2024-05-20",
      "end_date": "2024-05-26"
    },
    {
      "week": 26,
      "total_calories": 2913.6794999999997,
      "workout_count": 8,
      "start_date": "2024-06-25",
      "end_date": "2024-06-30"
    },
    {
      "week": 32,
      "total_calories": 2898.3043000000002,
      "workout_count": 10,
      "start_date": "2024-08-05",
      "end_date": "2024-08-11"
    },
    {
      "week": 45,
      "total_calories": 2707.612,
      "workout_count": 5,
      "start_date": "2024-11-04",
      "end_date": "2024-11-10"
    },
    {
      "week": 49,
      "total_calories": 2625.21,
      "workout_count": 10,
      "start_date": "2024-12-02",
      "end_date": "2024-12-08"
    },
    {
      "week": 34,
      "total_calories": 2591.8145,
      "workout_count": 8,
      "start_date": "2024-08-19",
      "end_date": "2024-08-25"
    },
    {
      "week": 51,
      "total_calories": 2533.359,
      "workout_count": 9,
      "start_date": "2024-12-17",
      "end_date": "2024-12-22"
    },
    {
      "week": 47,
      "total_calories": 2392.2828999999997,
      "workout_count": 10,
      "start_date": "2024-11-19",
      "end_date": "2024-11-24"
    },
    {
      "week": 50,
      "total_calories": 1769.9810000000002,
      "workout_count": 7,
      "start_date": "2024-12-09",
      "end_date": "2024-12-12"
    },
    {
      "week": 25,
      "total_calories": 1760.8376799999999,
      "workout_count": 8,
      "start_date": "2024-06-17",
      "end_date": "2024-06-23"
    },
    {
      "week": 39,
      "total_calories": 1464.4811,
      "workout_count": 5,
      "start_date": "2024-09-26",
      "end_date": "2024-09-29"
    },
    {
      "week": 52,
      "total_calories": 1408.9978999999998,
      "workout_count": 7,
      "start_date": "2024-12-23",
      "end_date": "2024-12-28"
    },
    {
      "week": 31,
      "total_calories": 1404.3019,
      "workout_count": 7,
      "start_date": "2024-07-29",
      "end_date": "2024-08-04"
    },
    {
      "week": 30,
      "total_calories": 1325.8763999999999,
      "workout_count": 7,
      "start_date": "2024-07-22",
      "end_date": "2024-07-28"
    },
    {
      "week": 19,
      "total_calories": 1159.5690000000002,
      "workout_count": 3,
      "start_date": "2024-05-07",
      "end_date": "2024-05-12"
    },
    {
      "week": 20,
      "total_calories": 1042.717,
      "workout_count": 3,
      "start_date": "2024-05-13",
      "end_date": "2024-05-19"
    },
    {
      "week": 46,
      "total_calories": 982.7710000000002,
      "workout_count": 4,
      "start_date": "2024-11-11",
      "end_date": "2024-11-17"
    },
    {
      "week": 16,
      "total_calories": 954.679,
      "workout_count": 1,
      "start_date": "2024-04-15",
      "end_date": "2024-04-15"
    },
    {
      "week": 36,
      "total_calories": 824.7039000000001,
      "workout_count": 4,
      "start_date": "2024-09-02",
      "end_date": "2024-09-04"
    },
    {
      "week": 42,
      "total_calories": 810.704,
      "workout_count": 4,
      "start_date": "2024-10-14",
      "end_date": "2024-10-19"
    },
    {
      "week": 40,
      "total_calories": 555.192,
      "workout_count": 2,
      "start_date": "2024-10-01",
      "end_date": "2024-10-04"
    },
    {
      "week": 38,
      "total_calories": 521.8953,
      "workout_count": 4,
      "start_date": "2024-09-17",
      "end_date": "2024-09-22"
    },
    {
      "week": 35,
      "total_calories": 469.16499999999996,
      "workout_count": 3,
      "start_date": "2024-08-26",
      "end_date": "2024-09-01"
    },
    {
      "week": 18,
      "total_calories": 400.657,
      "workout_count": 2,
      "start_date": "2024-05-01",
      "end_date": "2024-05-05"
    },
    {
      "week": 41,
      "total_calories": 394.925,
      "workout_count": 1,
      "start_date": "2024-10-11",
      "end_date": "2024-10-11"
    },
    {
      "week": 37,
      "total_calories": 269.1589,
      "workout_count": 2,
      "start_date": "2024-09-14",
      "end_date": "2024-09-14"
    },
    {
      "week": 13,
      "total_calories": 211.14,
      "workout_count": 1,
      "start_date": "2024-03-25",
      "end_date": "2024-03-25"
    },
    {
      "week": 12,
      "total_calories": 207.715,
      "workout_count": 1,
      "start_date": "2024-03-18",
      "end_date": "2024-03-18"
    },
    {
      "week": 44,
      "total_calories": 65.4385,
      "workout_count": 1,
      "start_date": "2024-10-30",
      "end_date": "2024-10-30"
    }
  ],
  "missed_workout_days_2024": [
    "2024-01-01",
    "2024-01-02",
    "2024-01-03",
    "2024-01-04",
    "2024-01-05",
    "2024-01-06",
    "2024-01-07",
    "2024-01-08",
    "2024-01-09",
    "2024-01-10",
    "2024-01-11",
    "2024-01-12",
    "2024-01-13",
    "2024-01-14",
    "2024-01-15",
    "2024-01-16",
    "2024-01-17",
    "2024-01-18",
    "2024-01-19",
    "2024-01-20",
    "2024-01-21",
    "2024-01-22",
    "2024-01-23",
    "2024-01-24",
    "2024-01-25",
    "2024-01-26",
    "2024-01-27",
    "2024-01-28",
    "2024-01-29",
    "2024-01-30",
    "2024-01-31",
    "2024-02-01",
    "2024-02-02",
    "2024-02-03",
    "2024-02-04",
    "2024-02-05",
    "2024-02-06",
    "2024-02-07",
    "2024-02-08",
    "2024-02-09",
    "2024-02-10",
    "2024-02-11",
    "2024-02-12",
    "2024-02-13",
    "2024-02-14",
    "2024-02-15",
    "2024-02-16",
    "2024-02-17",
    "2024-02-18",
    "2024-02-19",
    "2024-02-20",
    "2024-02-21",
    "2024-02-22",
    "2024-02-23",
    "2024-02-24",
    "2024-02-25",
    "2024-02-26",
    "2024-02-27",
    "2024-02-28",
    "2024-02-29",
    "2024-03-01",
    "2024-03-02",
    "2024-03-03",
    "2024-03-04",
    "2024-03-05",
    "2024-03-06",
    "2024-03-07",
    "2024-03-08",
    "2024-03-09",
    "2024-03-10",
    "2024-03-11",
    "2024-03-12",
    "2024-03-13",
    "2024-03-14",
    "2024-03-15",
    "2024-03-16",
    "2024-03-17",
    "2024-03-19",
    "2024-03-20",
    "2024-03-21",
    "2024-03-22",
    "2024-03-23",
    "2024-03-24",
    "2024-03-26",
    "2024-03-27",
    "2024-03-28",
    "2024-03-29",
    "2024-03-30",
    "2024-03-31",
    "2024-04-01",
    "2024-04-02",
    "2024-04-03",
    "2024-04-04",
    "2024-04-05",
    "2024-04-06",
    "2024-04-07",
    "2024-04-08",
    "2024-04-09",
    "2024-04-10",
    "2024-04-11",
    "2024-04-12",
    "2024-04-13",
    "2024-04-14",
    "2024-04-16",
    "2024-04-17",
    "2024-04-18",
    "2024-04-19",
    "2024-04-20",
    "2024-04-21",
    "2024-04-22",
    "2024-04-23",
    "2024-04-24",
    "2024-04-25",
    "2024-04-26",
    "2024-04-27",
    "2024-04-28",
    "2024-04-29",
    "2024-04-30",
    "2024-05-02",
    "2024-05-03",
    "2024-05-04",
    "2024-05-06",
    "2024-05-08",
    "2024-05-09",
    "2024-05-10",
    "2024-05-15",
    "2024-05-16",
    "2024-05-17",
    "2024-05-18",
    "2024-06-19",
    "2024-06-21",
    "2024-06-22",
    "2024-06-24",
    "2024-07-11",
    "2024-07-25",
    "2024-08-02",
    "2024-08-06",
    "2024-08-22",
    "2024-08-28",
    "2024-08-29",
    "2024-08-30",
    "2024-08-31",
    "2024-09-05",
    "2024-09-06",
    "2024-09-07",
    "2024-09-08",
    "2024-09-09",
    "2024-09-10",
    "2024-09-11",
    "2024-09-12",
    "2024-09-13",
    "2024-09-15",
    "2024-09-16",
    "2024-09-19",
    "2024-09-21",
    "2024-09-23",
    "2024-09-24",
    "2024-09-25",
    "2024-09-30",
    "2024-10-02",
    "2024-10-03",
    "2024-10-05",
    "2024-10-06",
    "2024-10-07",
    "2024-10-08",
    "2024-10-09",
    "2024-10-10",
    "2024-10-12",
    "2024-10-13",
    "2024-10-15",
    "2024-10-18",
    "2024-10-20",
    "2024-10-21",
    "2024-10-22",
    "2024-10-23",
    "2024-10-24",
    "2024-10-25",
    "2024-10-26",
    "2024-10-27",
    "2024-10-28",
    "2024-10-29",
    "2024-10-31",
    "2024-11-01",
    "2024-11-02",
    "2024-11-03",
    "2024-11-06",
    "2024-11-07",
    "2024-11-08",
    "2024-11-12",
    "2024-11-13",
    "2024-11-14",
    "2024-11-15",
    "2024-11-18",
    "2024-11-30",
    "2024-12-04",
    "2024-12-06",
    "2024-12-13",
    "2024-12-14",
    "2024-12-15",
    "2024-12-16",
    "2024-12-21",
    "2024-12-24",
    "2024-12-26",
    "2024-12-29",
    "2024-12-30",
    "2024-12-31"
  ],
  "average_heart_rate_2024": {
    "Cycling": {
      "average": 125.75,
      "highest": 181.0,
      "lowest": 64.0,
      "workout_count": 7
    },
    "Elliptical": {
      "average": 149.3,
      "highest": 189.0,
      "lowest": 95.0,
      "workout_count": 8
    },
    "FunctionalStrengthTraining": {
      "average": 112.8,
      "highest": 162.0,
      "lowest": 76.0,
      "workout_count": 4
    },
    "Golf": {
      "average": 89.29,
      "highest": 121.0,
      "lowest": 74.0,
      "workout_count": 3
    },
    "HighIntensityIntervalTraining": {
      "average": 136.98,
      "highest": 172.0,
      "lowest": 94.0,
      "workout_count": 1
    },
    "Hiking": {
      "average": 122.47,
      "highest": 178.0,
      "lowest": 86.0,
      "workout_count": 3
    },
    "PaddleSports": {
      "average": 104.74,
      "highest": 143.0,
      "lowest": 81.0,
      "workout_count": 1
    },
    "Pickleball": {
      "average": 142.32,
      "highest": 197.0,
      "lowest": 77.0,
      "workout_count": 32
    },
    "Running": {
      "average": 108.67,
      "highest": 120.0,
      "lowest": 95.0,
      "workout_count": 1
    },
    "Tennis": {
      "average": 127.14,
      "highest": 187.0,
      "lowest": 76.0,
      "workout_count": 2
    },
    "TraditionalStrengthTraining": {
      "average": 113.56,
      "highest": 173.0,
      "lowest": 63.0,
      "workout_count": 42
    },
    "Walking": {
      "average": 114.04,
      "highest": 185.0,
      "lowest": 62.0,
      "workout_count": 122
    }
  },
  "monthly_workouts": {
    "month_3": {
      "count": 2,
      "calories": 418.86
    },
    "month_4": {
      "count": 1,
      "calories": 954.68
    },
    "month_5": {
      "count": 25,
      "calories": 7684.23
    },
    "month_6": {
      "count": 42,
      "calories": 13854.95
    },
    "month_7": {
      "count": 35,
      "calories": 14731.55
    },
    "month_8": {
      "count": 32,
      "calories": 9804.45
    },
    "month_9": {
      "count": 16,
      "calories": 3254.49
    },
    "month_10": {
      "count": 8,
      "calories": 1826.26
    },
    "month_11": {
      "count": 30,
      "calories": 8787.13
    },
    "month_12": {
      "count": 35,
      "calories": 8821.01
    }
  }
}
```