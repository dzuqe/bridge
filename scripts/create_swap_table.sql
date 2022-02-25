create if not exists table swap
(
    id: int,
    sender: varchar(255),
    receiver: varchar(255),
    sent_txid: boolean,
    rcvd_txid: boolean,
    withdrew: boolean,
);
