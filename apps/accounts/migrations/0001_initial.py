# Generated by Django 4.2.4 on 2023-10-02 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("user_id", models.CharField(max_length=50, unique=True)),
                ("language_choice", models.CharField(max_length=3)),
                ("first_name", models.CharField(blank=True, max_length=30, null=True)),
                ("last_name", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "chosen_language",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "wallet_address",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "wallet_private_key",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "wallet_phrase",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "wallet_gas",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                (
                    "eth_balance",
                    models.DecimalField(decimal_places=4, default=0.0, max_digits=20),
                ),
                (
                    "bsc_balance",
                    models.DecimalField(decimal_places=4, default=0.0, max_digits=20),
                ),
                (
                    "arp_balance",
                    models.DecimalField(decimal_places=4, default=0.0, max_digits=20),
                ),
                (
                    "base_balance",
                    models.DecimalField(decimal_places=4, default=0.0, max_digits=20),
                ),
                (
                    "eth_preset",
                    models.CharField(
                        choices=[
                            ("FAST", "FAST"),
                            ("SLOW", "SLOW"),
                            ("AVERAGE", "AVERAGE"),
                            ("MAX_SPEED", "MAX_SPEED"),
                        ],
                        default="AVERAGE",
                        max_length=15,
                    ),
                ),
                (
                    "bsc_preset",
                    models.CharField(
                        choices=[
                            ("FAST", "FAST"),
                            ("SLOW", "SLOW"),
                            ("AVERAGE", "AVERAGE"),
                            ("MAX_SPEED", "MAX_SPEED"),
                        ],
                        default="AVERAGE",
                        max_length=15,
                    ),
                ),
                (
                    "arp_preset",
                    models.CharField(
                        choices=[
                            ("FAST", "FAST"),
                            ("SLOW", "SLOW"),
                            ("AVERAGE", "AVERAGE"),
                            ("MAX_SPEED", "MAX_SPEED"),
                        ],
                        default="AVERAGE",
                        max_length=15,
                    ),
                ),
                (
                    "base_preset",
                    models.CharField(
                        choices=[
                            ("FAST", "FAST"),
                            ("SLOW", "SLOW"),
                            ("AVERAGE", "AVERAGE"),
                            ("MAX_SPEED", "MAX_SPEED"),
                        ],
                        default="AVERAGE",
                        max_length=15,
                    ),
                ),
                ("BSC_added", models.BooleanField(default=False)),
                ("ARB_added", models.BooleanField(default=False)),
                ("BASE_added", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("agreed_to_terms", models.BooleanField(default=True)),
                (
                    "max_gas",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
                ),
                (
                    "max_gas_price",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
                ),
                (
                    "max_delta",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
                ),
                (
                    "slippage",
                    models.DecimalField(decimal_places=2, default=20.0, max_digits=20),
                ),
                (
                    "buy_tax",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
                ),
                (
                    "sell_tax",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
                ),
                (
                    "sell_hi",
                    models.DecimalField(decimal_places=2, default=2.0, max_digits=20),
                ),
                (
                    "sell_lo",
                    models.DecimalField(decimal_places=2, default=0.5, max_digits=20),
                ),
                (
                    "sell_hi_amount",
                    models.DecimalField(decimal_places=2, default=20.0, max_digits=20),
                ),
                (
                    "sell_lo_amount",
                    models.DecimalField(decimal_places=2, default=0.2, max_digits=20),
                ),
                ("auto_sell", models.BooleanField(default=False)),
                ("dupe_buy", models.BooleanField(default=False)),
                ("auto_buy", models.BooleanField(default=False)),
                ("auto_approve", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="copytradetxhash",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.CharField(blank=True, max_length=500)),
                ("txhash", models.CharField(blank=True, max_length=500)),
                ("bot_name", models.CharField(blank=True, max_length=500)),
                (
                    "amount",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                ("token_address", models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="TradeAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.CharField(blank=True, max_length=500)),
                ("token_address", models.CharField(blank=True, max_length=500)),
                ("token_name", models.CharField(blank=True, max_length=500)),
                ("chain", models.CharField(blank=True, max_length=500)),
                (
                    "limit",
                    models.DecimalField(decimal_places=10, default=0.0, max_digits=20),
                ),
                ("check_limit", models.BooleanField(default=False)),
                (
                    "profit",
                    models.DecimalField(decimal_places=10, default=0.0, max_digits=20),
                ),
                ("check_profit", models.BooleanField(default=False)),
                (
                    "stop_loss",
                    models.DecimalField(decimal_places=10, default=0.0, max_digits=20),
                ),
                ("check_stop_loss", models.BooleanField(default=False)),
                (
                    "gas_delta",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                (
                    "slippage",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                (
                    "ammount_limit",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
            ],
        ),
        migrations.CreateModel(
            name="tradetxhash",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.CharField(blank=True, max_length=500)),
                ("txhash", models.CharField(blank=True, max_length=500)),
                ("bot_name", models.CharField(blank=True, max_length=500)),
                (
                    "amount",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                ("token_address", models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Txhash",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Txhash", models.CharField(blank=True, max_length=500)),
                ("user_id", models.CharField(blank=True, max_length=500)),
                ("check_txhash", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Sniper",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chain", models.CharField(blank=True, max_length=5)),
                ("name", models.CharField(blank=True, max_length=255)),
                ("symbol", models.CharField(blank=True, max_length=255)),
                ("decimal", models.IntegerField(default=18)),
                ("contract_address", models.CharField(blank=True, max_length=500)),
                ("auto", models.BooleanField(default=False)),
                ("method", models.BooleanField(default=False)),
                ("liquidity", models.BooleanField(default=False)),
                (
                    "block_delay",
                    models.DecimalField(decimal_places=6, default=0, max_digits=12),
                ),
                (
                    "eth",
                    models.DecimalField(decimal_places=6, default=1, max_digits=12),
                ),
                (
                    "token",
                    models.DecimalField(decimal_places=6, default=10, max_digits=12),
                ),
                ("multi", models.BooleanField(default=False)),
                ("buy", models.BooleanField(default=True)),
                ("enable", models.BooleanField(default=True)),
                ("stop", models.BooleanField(default=False)),
                ("approve", models.BooleanField(default=True)),
                ("auto_sell", models.BooleanField(default=True)),
                ("buy_dip", models.BooleanField(default=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sniper",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CopyTradeAddresses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chain", models.CharField(blank=True, max_length=5)),
                ("name", models.CharField(blank=True, max_length=250)),
                ("contract_address", models.CharField(blank=True, max_length=500)),
                ("on", models.BooleanField(default=False)),
                ("multi", models.BooleanField(default=False)),
                ("auto_buy", models.BooleanField(default=False)),
                ("copy_sell", models.BooleanField(default=False)),
                ("smart_slippage", models.BooleanField(default=True)),
                (
                    "amount",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                (
                    "slippage",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                (
                    "gas_delta",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                (
                    "sell_hi_amount",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                (
                    "sell_lo_amount",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                (
                    "sell_hi",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                (
                    "sell_lo",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                (
                    "max_buy_tax",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                (
                    "max_sell_tax",
                    models.DecimalField(decimal_places=6, default=0.0, max_digits=20),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="copy_trades",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
