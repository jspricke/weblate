# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.1.1 on 2020-10-02 14:18

from django.db import migrations


def migrate_screenshot(apps, schema_editor):
    Screenshot = apps.get_model("screenshots", "Screenshot")
    db_alias = schema_editor.connection.alias
    for screenshot in Screenshot.objects.using(db_alias).prefetch_related("component"):
        component = screenshot.component
        screenshot.translation = component.translation_set.get(
            language_id=component.source_language_id
        )
        screenshot.save(update_fields=["translation"])


class Migration(migrations.Migration):
    dependencies = [
        ("screenshots", "0002_screenshot_translation"),
        ("trans", "0099_remove_project_source_language"),
    ]

    operations = [migrations.RunPython(migrate_screenshot, elidable=True)]
