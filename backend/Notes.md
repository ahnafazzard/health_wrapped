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
