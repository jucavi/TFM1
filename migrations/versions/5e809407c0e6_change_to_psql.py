"""change to psql

Revision ID: 5e809407c0e6
Revises: 
Create Date: 2022-04-13 09:56:45.049128

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5e809407c0e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('filename', sa.String(length=50), nullable=True),
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('mimetype', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_file_filename'), 'file', ['filename'], unique=False)
    op.create_index(op.f('ix_file_id'), 'file', ['id'], unique=False)
    op.create_table('project',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('project_name', sa.String(length=40), nullable=True),
    sa.Column('project_desc', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_project_id'), 'project', ['id'], unique=False)
    op.create_index(op.f('ix_project_project_name'), 'project', ['project_name'], unique=True)
    op.create_table('user',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('firstname', sa.String(length=40), nullable=False),
    sa.Column('lastname', sa.String(length=40), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('last_message_read_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_firstname'), 'user', ['firstname'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_lastname'), 'user', ['lastname'], unique=False)
    op.create_index(op.f('ix_user_password'), 'user', ['password'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('folder',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('foldername', sa.String(length=50), nullable=False),
    sa.Column('parent_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['folder.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_folder_foldername'), 'folder', ['foldername'], unique=False)
    op.create_index(op.f('ix_folder_id'), 'folder', ['id'], unique=False)
    op.create_table('message',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('sender_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('recipient_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('subject', sa.String(length=100), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('read', sa.Boolean(), nullable=True),
    sa.Column('deleted_by_recipient', sa.Boolean(), nullable=True),
    sa.Column('deleted_by_author', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['recipient_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_id'), 'message', ['id'], unique=False)
    op.create_index(op.f('ix_message_timestamp'), 'message', ['timestamp'], unique=False)
    op.create_table('team',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('project_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('is_owner', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_team_id'), 'team', ['id'], unique=False)
    op.create_table('folder_content',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('folder_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('file_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.ForeignKeyConstraint(['folder_id'], ['folder.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_folder_content_id'), 'folder_content', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_folder_content_id'), table_name='folder_content')
    op.drop_table('folder_content')
    op.drop_index(op.f('ix_team_id'), table_name='team')
    op.drop_table('team')
    op.drop_index(op.f('ix_message_timestamp'), table_name='message')
    op.drop_index(op.f('ix_message_id'), table_name='message')
    op.drop_table('message')
    op.drop_index(op.f('ix_folder_id'), table_name='folder')
    op.drop_index(op.f('ix_folder_foldername'), table_name='folder')
    op.drop_table('folder')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_password'), table_name='user')
    op.drop_index(op.f('ix_user_lastname'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_firstname'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_project_project_name'), table_name='project')
    op.drop_index(op.f('ix_project_id'), table_name='project')
    op.drop_table('project')
    op.drop_index(op.f('ix_file_id'), table_name='file')
    op.drop_index(op.f('ix_file_filename'), table_name='file')
    op.drop_table('file')
    # ### end Alembic commands ###
