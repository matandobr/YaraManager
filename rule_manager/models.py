from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=200, null=True, blank=True)


class Rule(models.Model):
    rule_name = models.CharField(max_length=200)
    rule_description = models.CharField(max_length=200, null=True, blank=True)
    rule_category = models.CharField(max_length=200, null=True, blank=True)
    rule_source = models.CharField(max_length=200, null=True, blank=True)
    rule_version = models.IntegerField(default=0)
    rule_created = models.DateTimeField(auto_now_add=True)
    rule_edited = models.DateTimeField(auto_now_add=True)
    rule_state = models.IntegerField(default=0)
    rule_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.rule_name


class MetaData(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=200, null=True, blank=True)
    meta_value = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.rule.rule_name


class RuleStrings(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    string_type = models.CharField(max_length=20, default='text')
    string_name = models.CharField(max_length=200)
    string_value = models.CharField(max_length=1000)
    string_nocase = models.BooleanField(default=False)
    string_wide = models.BooleanField(default=False)
    string_full = models.BooleanField(default=False)
    string_ascii = models.BooleanField(default=False)
    
    def __str__(self):
        return self.rule.rule_name


class Condition(models.Model):
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    condition = models.CharField(max_length=200)
    
    def __str__(self):
        return self.rule.rule_name