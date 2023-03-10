"""Init

Revision ID: fda6ad58bd8f
Revises: 
Create Date: 2022-12-09 01:52:30.719439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fda6ad58bd8f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cashiers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cashier_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cashiers_id'), 'cashiers', ['id'], unique=False)
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_name', sa.String(), nullable=True),
    sa.Column('passport', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_clients_id'), 'clients', ['id'], unique=False)
    op.create_table('currencies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('currency_name', sa.String(), nullable=True),
    sa.Column('currency_rate', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_currencies_id'), 'currencies', ['id'], unique=False)
    op.create_table('deals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deal_date', sa.DateTime(), nullable=True),
    sa.Column('sum', sa.Integer(), nullable=True),
    sa.Column('sold', sa.Boolean(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('currency_id', sa.Integer(), nullable=True),
    sa.Column('cashier_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cashier_id'], ['cashiers.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['currency_id'], ['currencies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_deals_id'), 'deals', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_deals_id'), table_name='deals')
    op.drop_table('deals')
    op.drop_index(op.f('ix_currencies_id'), table_name='currencies')
    op.drop_table('currencies')
    op.drop_index(op.f('ix_clients_id'), table_name='clients')
    op.drop_table('clients')
    op.drop_index(op.f('ix_cashiers_id'), table_name='cashiers')
    op.drop_table('cashiers')
    # ### end Alembic commands ###
