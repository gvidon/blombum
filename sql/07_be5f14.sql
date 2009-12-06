ALTER TABLE blog_post ADD COLUMN site_id integer NULL REFERENCES django_site (id)  DEFERRABLE INITIALLY DEFERRED;
UPDATE blog_post SET site_id = (SELECT id FROM django_site ORDER BY id LIMIT 1);
ALTER TABLE blog_post ALTER COLUMN site_id SET NOT NULL;
CREATE INDEX blog_post_site_id ON blog_post (site_id);
