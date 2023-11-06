# nakayama
test
##サッカーの情報サイト
このサイトはプレミアリーグのBIG6のサイトです!!


## ER図
```mermaid
erDiagram
    USER ||--o{ FAVORITE_TEAM : chooses
    TEAM ||--o{ FAVORITE_TEAM : chosen_by
    TEAM ||--o{ PLAYERS : includes
    TEAM ||--o{ MATCHES : "participates in"
    PLAYERS ||--o{ MATCHES : "plays in"
    
    USER {
        string id PK "ユーザーID"
        string password "パスワード"
        string email "メールアドレス"
        string username "ユーザーネーム"
    }
    TEAM {
        string id PK "チームID"
        string name "チーム名"
        string location "所在地"
    }
    FAVORITE_TEAM {
        string userID FK "ユーザーID"
        string teamID FK "チームID"
    }
    PLAYERS {
        string id PK "選手ID"
        string teamID FK "チームID"
        string name "名前"
        string position "ポジション"
        int number "背番号"
    }
    MATCHES {
        string id PK "試合ID"
        string homeTeamID FK "ホームチームID"
        string awayTeamID FK "アウェイチームID"
        date matchDate "開催日"
        string score "スコア"
    }


```