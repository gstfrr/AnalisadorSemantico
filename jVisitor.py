# Generated from /Users/augusto/PycharmProjects/AnalisadorSemantico/j.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jParser import jParser
else:
    from jParser import jParser

# This class defines a complete generic visitor for a parse tree produced by jParser.

class jVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jParser#compilationUnit.
    def visitCompilationUnit(self, ctx:jParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#qualifiedIdentifier.
    def visitQualifiedIdentifier(self, ctx:jParser.QualifiedIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:jParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#modifiers.
    def visitModifiers(self, ctx:jParser.ModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#classDeclaration.
    def visitClassDeclaration(self, ctx:jParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#classBody.
    def visitClassBody(self, ctx:jParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#memberDecl.
    def visitMemberDecl(self, ctx:jParser.MemberDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#block.
    def visitBlock(self, ctx:jParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#blockStatement.
    def visitBlockStatement(self, ctx:jParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#statement.
    def visitStatement(self, ctx:jParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#formalParameters.
    def visitFormalParameters(self, ctx:jParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#formalParameter.
    def visitFormalParameter(self, ctx:jParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#parExpression.
    def visitParExpression(self, ctx:jParser.ParExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#localVariableDeclarationStatement.
    def visitLocalVariableDeclarationStatement(self, ctx:jParser.LocalVariableDeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#variableDeclarators.
    def visitVariableDeclarators(self, ctx:jParser.VariableDeclaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:jParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#variableInitializer.
    def visitVariableInitializer(self, ctx:jParser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#arrayInitializer.
    def visitArrayInitializer(self, ctx:jParser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#arguments.
    def visitArguments(self, ctx:jParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#typ.
    def visitTyp(self, ctx:jParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#basicType.
    def visitBasicType(self, ctx:jParser.BasicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#referenceType.
    def visitReferenceType(self, ctx:jParser.ReferenceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#statementExpression.
    def visitStatementExpression(self, ctx:jParser.StatementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#expression.
    def visitExpression(self, ctx:jParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:jParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#conditionalAndExpression.
    def visitConditionalAndExpression(self, ctx:jParser.ConditionalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#equalityExpression.
    def visitEqualityExpression(self, ctx:jParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#relationalExpression.
    def visitRelationalExpression(self, ctx:jParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:jParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:jParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#unaryExpression.
    def visitUnaryExpression(self, ctx:jParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#simpleUnaryExpression.
    def visitSimpleUnaryExpression(self, ctx:jParser.SimpleUnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#postfixExpression.
    def visitPostfixExpression(self, ctx:jParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#selector.
    def visitSelector(self, ctx:jParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#primary.
    def visitPrimary(self, ctx:jParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#creator.
    def visitCreator(self, ctx:jParser.CreatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#newArrayDeclarator.
    def visitNewArrayDeclarator(self, ctx:jParser.NewArrayDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jParser#literal.
    def visitLiteral(self, ctx:jParser.LiteralContext):
        return self.visitChildren(ctx)



del jParser