ALTER TABLE blogroll_link ADD COLUMN site_id integer NULL REFERENCES django_site (id)  DEFERRABLE INITIALLY DEFERRED;
UPDATE blogroll_link SET site_id = (SELECT id FROM django_site ORDER BY id LIMIT 1);
ALTER TABLE blogroll_link ALTER COLUMN site_id SET NOT NULL;
CREATE INDEX blogroll_link_site_id ON blogroll_link (site_id);
