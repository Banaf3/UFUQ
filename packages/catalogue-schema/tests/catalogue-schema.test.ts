import { describe, expect, it } from 'vitest';

import {
  HIPPARCOS_I311_MAIN_FIELD_CONTRACT_V1,
  HIPPARCOS_I311_MAIN_RECORD_SCHEMA_V1,
  HIPPARCOS_I311_SOURCE_V1,
  HIPPARCOS_I311_SUPPLEMENT_SCHEMA_V1,
} from '../src/catalogue/index.js';
import {
  CATALOGUE_ARTIFACT_SCHEMA_V1,
  CATALOGUE_CANONICAL_SERIALIZATION_V1,
  CATALOGUE_PROVENANCE_MANIFEST_SCHEMA_V1,
} from '../src/artifact/index.js';

describe('catalogue metadata contracts', () => {
  it('names I/311 right-ascension proper motion as mu_alpha_star without ambiguity', () => {
    expect(HIPPARCOS_I311_SOURCE_V1.rightAscensionProperMotion).toEqual({
      sourceLabel: 'pmRA',
      sourceSymbol: 'mu_alpha_star',
      normalizedField: 'properMotionRaCosDecMilliarcsecondsPerYear',
      unit: 'mas/yr',
    });

    const pmRaField = HIPPARCOS_I311_MAIN_FIELD_CONTRACT_V1.find(
      ({ sourceLabel }) => sourceLabel === 'pmRA',
    );
    expect(pmRaField?.normalizedField).toBe('properMotionRaCosDecMilliarcsecondsPerYear');
    expect(HIPPARCOS_I311_MAIN_RECORD_SCHEMA_V1.properties).not.toHaveProperty(
      'properMotionRaMilliarcsecondsPerYear',
    );
  });

  it('retains all official main-table fields and supplementary solution families', () => {
    expect(HIPPARCOS_I311_MAIN_FIELD_CONTRACT_V1).toHaveLength(27);
    expect(HIPPARCOS_I311_MAIN_FIELD_CONTRACT_V1.at(-1)).toMatchObject({
      sourceLabel: 'UW',
      byteRange: '172-276',
      normalizedField: 'upperTriangularWeightMatrixSourceValues',
    });

    const supplementKinds = HIPPARCOS_I311_SUPPLEMENT_SCHEMA_V1.oneOf.map(
      ({ properties }) => properties.kind.const,
    );
    expect(supplementKinds).toEqual(['SEVEN_PARAMETER', 'NINE_PARAMETER', 'VIM']);
    expect(HIPPARCOS_I311_MAIN_RECORD_SCHEMA_V1.allOf).toHaveLength(4);
  });

  it('keeps cultural and instructional content outside numerical schemas', () => {
    const numericalSchemas = JSON.stringify([
      HIPPARCOS_I311_MAIN_RECORD_SCHEMA_V1,
      HIPPARCOS_I311_SUPPLEMENT_SCHEMA_V1,
      CATALOGUE_ARTIFACT_SCHEMA_V1,
    ]).toLowerCase();

    for (const prohibitedTerm of [
      'arabicname',
      'transliteration',
      'asterism',
      'linesegment',
      'teachingrole',
    ]) {
      expect(numericalSchemas).not.toContain(prohibitedTerm);
    }
  });

  it('pins source identity while preserving the unresolved epoch time scale', () => {
    expect(HIPPARCOS_I311_SOURCE_V1).toMatchObject({
      catalogueId: 'CDS_I311',
      tableId: 'hip2.dat',
      archiveVariant: 'AUTHOR_REPLACEMENT_2008-09-16',
      referenceFrame: 'ICRS',
      referenceEpoch: {
        sourceNotation: 'Ep=1991.25',
        value: 1991.25,
        timeScale: 'UNSPECIFIED_BY_I311_METADATA',
      },
    });
  });
});

describe('canonical catalogue artifact contracts', () => {
  it('defines deterministic serialization independently of host and Git settings', () => {
    expect(CATALOGUE_CANONICAL_SERIALIZATION_V1).toEqual({
      encoding: 'UTF-8',
      byteOrderMark: false,
      unicodeNormalization: 'NFC',
      lineEnding: 'LF',
      trailingLineFeed: true,
      objectKeyOrder: 'LEXICOGRAPHIC_ASCENDING',
      recordOrder: 'HIP_ID_NUMERIC_ASCENDING',
      arrayOrder: 'SCHEMA_DEFINED',
      numberFormat: 'SHORTEST_ROUND_TRIP_JSON_NUMBER',
      negativeZero: 'NORMALIZE_TO_ZERO',
      nonFiniteNumbers: 'REJECT',
      volatileFieldsInCanonicalPayload: false,
    });
  });

  it('requires licence, input identity, selection evidence, and output checksum', () => {
    expect(CATALOGUE_PROVENANCE_MANIFEST_SCHEMA_V1.required).toEqual(
      expect.arrayContaining([
        'source',
        'licence',
        'selection',
        'generator',
        'schemas',
        'canonicalSerialization',
        'artifact',
      ]),
    );
    expect(
      CATALOGUE_PROVENANCE_MANIFEST_SCHEMA_V1.properties.licence.properties.redistributionDecision
        .enum,
    ).toContain('BLOCK_TRACKING_AND_DEPLOYMENT');
    expect(CATALOGUE_PROVENANCE_MANIFEST_SCHEMA_V1.properties.source.required).toEqual(
      expect.arrayContaining(['acquiredAtUtc', 'acquisitionMethod', 'rawFiles']),
    );
  });

  it('requires unique HIP identifiers in an explicitly reviewed selection', () => {
    expect(CATALOGUE_ARTIFACT_SCHEMA_V1.properties.selection.properties.hipIds).toMatchObject({
      type: 'array',
      minItems: 1,
      uniqueItems: true,
    });
    expect(
      CATALOGUE_ARTIFACT_SCHEMA_V1.properties.selection.properties.approvalStatus.enum,
    ).toEqual(['TECHNICAL_CANDIDATE_ONLY', 'DOMAIN_APPROVED']);
  });
});
