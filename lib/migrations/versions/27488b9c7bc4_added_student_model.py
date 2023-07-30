"""Added Student model

Revision ID: 27488b9c7bc4
Revises: 62ad6217885a
Create Date: 2023-07-26 13:17:09.082438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27488b9c7bc4'
down_revision = '62ad6217885a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=40), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=True),
    sa.Column('species', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('adoptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_and_time', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('pet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['owners.id'], name=op.f('fk_adoptions_owner_id_owners')),
    sa.ForeignKeyConstraint(['pet_id'], ['pets.id'], name=op.f('fk_adoptions_pet_id_pets')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owners_stats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('money', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['owners.id'], name=op.f('fk_owners_stats_owner_id_owners')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pets_stats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('happiness', sa.Integer(), nullable=True),
    sa.Column('love', sa.Integer(), nullable=True),
    sa.Column('hunger', sa.Integer(), nullable=True),
    sa.Column('rowdiness', sa.Integer(), nullable=True),
    sa.Column('pet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pet_id'], ['pets.id'], name=op.f('fk_pets_stats_pet_id_pets')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('actions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_and_time', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('service', sa.String(length=40), nullable=True),
    sa.Column('adoption_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['adoption_id'], ['adoptions.id'], name=op.f('fk_actions_adoption_id_adoptions')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('actions')
    op.drop_table('pets_stats')
    op.drop_table('owners_stats')
    op.drop_table('adoptions')
    op.drop_table('pets')
    op.drop_table('owners')
    # ### end Alembic commands ###