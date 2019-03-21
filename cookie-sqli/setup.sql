DROP TABLE IF EXISTS admins;
CREATE TABLE IF NOT EXISTS admins (
    id INT PRIMARY KEY,
    email TEXT NOT NULL,
    password TEXT,
    session TEXT
);

INSERT INTO admins VALUES 
    (0, 'admin@ns.agency', 'bernie_sanders_4_president', '76f46c14b962e97feeea194630efa1196f474e7bd53daa873be5a3fb3df9e2f0');
