CREATE KEYSPACE CPG
WITH REPLICATION={
    'class':'SimpleStrategy',
    'replication_factor':1
};

CREATE TABLE CPG.tracked_files (
    file_id UUID, 
    path text Primary Key,
    tracking_enabled boolean,
    latest_version int
);

CREATE TABLE CPG.versions(
    file_id UUID,
    version_id int,
    commit_time timestamp,
    author text,
    hash text,
    Primary Key (file_id,version_id)
);

CREATE TABLE CPG.tags(
    file_id uuid,
    version_id int,  
    tags set<text>,
    Primary Key(file_id,version_id)
);